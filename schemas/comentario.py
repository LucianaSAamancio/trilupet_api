"Luciana"
from pydantic import BaseModel


class ComentarioSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    servico_id: int = 1
    texto: str = "Aqui seu pet se senti em casa!"