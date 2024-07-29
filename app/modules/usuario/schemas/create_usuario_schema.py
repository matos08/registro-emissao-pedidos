from fastapi_camelcase import CamelModel


class CreateUsuarioSchema(CamelModel):
    name: str
    email: str
    password: str
