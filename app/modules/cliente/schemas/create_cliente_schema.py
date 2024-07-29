from fastapi_camelcase import CamelModel


class CreateClienteSchema(CamelModel):
    name: str
    email: str
    address: str
    telephone: str
