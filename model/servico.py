"Luciana"
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Servico(Base):
    __tablename__ = 'servico'

    id = Column("pk_servico", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    tipoDeServico = Column(String(140))
    valorDoServico = Column(Float)
    contato = Column(Integer)
    maisInformacoes = Column(String(140))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o serviço e o comentário.
    # Essa relação é implicita, não está salva na tabela 'servico',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, tipoDeServico:str, valorDoServico:float,
                 contato:Integer, maisInformacoes:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Servico

        Arguments:
            nome: nome do serviço.
            tipoDeServico: tipo de serviço oferecido para pet.
            valorDoServico: valor esperado para o serviço.
            contato: telefone para entrar em contato para o serviço.
            maisInformacoes: mais informações sobre o serviço.
            data_insercao: data de quando o serviço foi inserido à base.
        """
        self.nome = nome
        self.tipoDeServico = tipoDeServico
        self.valorDoServico = valorDoServico
        self.contato = contato
        self.maisInformacoes = maisInformacoes

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Serviço
        """
        self.comentarios.append(comentario)