from fastapi_camelcase import CamelModel


class UpdateClienteSchema(CamelModel):
    name: str
    email: str
    address: str
    telephone: str
