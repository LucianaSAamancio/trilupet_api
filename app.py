from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

#from model import Session, Produto, Comentario
from model import Session, Servico, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API de Servico", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
servico_tag = Tag(name="Serviço", description="Adição, visualização e remoção de serviços à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um serviços cadastrado na base")

#produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")
#comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/servico', tags=[servico_tag],
          responses={"200": ServicoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_servico(form: ServicoSchema):
    """Adiciona um novo Servico à base de dados

    Retorna uma representação dos servicos e comentários associados.
    """
    servico = Servico(
        nome=form.nome,
        tipoDeServico=form.tipoDeServico,
        valorDoServico=form.valorDoServico,
        contato=form.contato,
        maisInformacoes = form.maisInformacoes)
    logger.debug(f"Adicionando servico de nome: '{servico.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando serviço
        session.add(servico)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado servico de nome: '{servico.nome}'")
        return apresenta_servico(servico), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Serviço de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar serviço '{servico.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo serviço :/"
        logger.warning(f"Erro ao adicionar serviço '{servico.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/servico', tags=[servico_tag],
         responses={"200": ListagemServicosSchema, "404": ErrorSchema})
def get_servicos():
    """Faz a busca por todos os Serviços cadastrados

    Retorna uma representação da listagem de serviços.
    """
    logger.debug(f"Coletando serviços ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    servicos = session.query(Servico).all()

    if not servicos:
        # se não há serviços cadastrados
        return {"servicos": []}, 200
    else:
        logger.debug(f"%d serviços encontrados" % len(servicos))
        # retorna a representação de serviço
        print(servicos)
        return apresenta_servicos(servicos), 200


@app.get('/servico', tags=[servico_tag],
         responses={"200": ServicoViewSchema, "404": ErrorSchema})
def get_servico(query: ServicoBuscaSchema):
    """Faz a busca por um Serviço a partir do id do serviço

    Retorna uma representação dos serviços e comentários associados.
    """
    servico_nome = query.nome
    logger.debug(f"Coletando dados sobre serviço #{servico_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    servico = session.query(Servico).filter(Servico.nome == servico_nome).first()

    if not servico:
        # se o servico não foi encontrado
        error_msg = "Servico não encontrado na base :/"
        logger.warning(f"Erro ao buscar servico '{servico_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Serviço econtrado: '{servico.nome}'")
        # retorna a representação de serviço
        return apresenta_servico(servico), 200


@app.delete('/servico', tags=[servico_tag],
            responses={"200": ServicoDelSchema, "404": ErrorSchema})
def del_servico(query: ServicoBuscaSchema):
    """Deleta um Serviço a partir do nome de serviço informado

    Retorna uma mensagem de confirmação da remoção.
    """
    servico_nome = unquote(unquote(query.nome))
    print(servico_nome)
    logger.debug(f"Deletando dados sobre serviço #{servico_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Servico).filter(Servico.nome == servico_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado serviço #{servico_nome}")
        return {"mesage": "Serviço removido", "id": servico_nome}
    else:
        # se o serviço não foi encontrado
        error_msg = "Serviço não encontrado na base :/"
        logger.warning(f"Erro ao deletar serviço #'{servico_nome}', {error_msg}")
        return {"mesage": error_msg}, 404


@app.post('/cometario', tags=[comentario_tag],
          responses={"200": ServicoViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    """Adiciona de um novo comentário à um serviço cadastrado na base identificado pelo id

    Retorna uma representação dos serviços e comentários associados.
    """
    servico_id  = form.servico_id
    logger.debug(f"Adicionando comentários ao serviço #{servico_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo serviço
    servico = session.query(Servico).filter(Servico.id == servico_id).first()

    if not servico:
        # se serviço não encontrado
        error_msg = "Serviço não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao serviço '{servico_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao serviço
    servico.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário ao serviço #{servico_id}")

    # retorna a representação de serviço
    return apresenta_servico(servico), 200
