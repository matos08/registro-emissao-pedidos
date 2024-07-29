from fastapi_camelcase import CamelModel


class UpdateClienteSchema(CamelModel):
    email: str
    address: str
    telephone: str
