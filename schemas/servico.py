"Luciana"

from pydantic import BaseModel
from typing import Optional, List
from model.servico import Servico

from schemas import ComentarioSchema


class ServicoSchema(BaseModel):
    """ Define como um novo serviço a ser inserido deve ser representado
    """
    nome: str = "Creche para pet"
    tipoDeServico: str = "Creche"
    valorDoServico: float = 50.00
    contato: Optional[int] = 21911112222
    maisInformacoes: str = "Acesse o site"

class ServicoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do serviço.
    """
    nome: str = "Teste"


class ListagemServicosSchema(BaseModel):
    """ Define como uma listagem de serviços será retornada.
    """
    servicos:List[ServicoSchema]


def apresenta_servicos(servicos: List[Servico]):
    """ Retorna uma representação do serviço seguindo o schema definido em
        ServicoViewSchema.
    """
    result = []
    for servico in servicos:
        result.append({
            "nome": servico.nome,
            "tipoDeServico":servico.tipoDeServico,
            "valorDoServico":servico.valorDoServico,
            "contato":servico.contato,
            "maisInformacoes":servico.maisInformacoes,
        })

    return {"servicos": result}


class ServicoViewSchema(BaseModel):
    """ Define como um servico será retornado: servico + comentários.
    """
    id: int = 1
    nome: str = "Creche para pet"
    tipoDeServico: str = "Creche"
    valorDoServico: float = 50.00
    contato: Optional[int] = 21911112222
    maisInformacoes: str = "Site"
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class ServicoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_servico(servico: Servico):
    """ Retorna uma representação do servico seguindo o schema definido em
        ServicoViewSchema.
    """
    return {
        "id": servico.id,
        "nome": servico.nome,
        "tipoDeServico": servico.tipoDeServico,
        "valorDoServico":servico.valorDoServico, 
        "contato":servico.contato,
        "maisInformacoes":servico.maisInformacoes,
        "total_comentarios": len(servico.comentarios),
        "comentarios": [{"texto": c.texto} for c in servico.comentarios]
    }