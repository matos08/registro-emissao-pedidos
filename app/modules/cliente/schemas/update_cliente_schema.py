from fastapi_camelcase import CamelModel


class UpdateClienteSchema(CamelModel):
    nome: str
    email: str
    address: str
    telephone: str
