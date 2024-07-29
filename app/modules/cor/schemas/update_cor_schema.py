from fastapi_camelcase import CamelModel


class UpdateCorSchema(CamelModel):
    nome: str
    value: float
