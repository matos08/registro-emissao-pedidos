from fastapi_camelcase import CamelModel


class UpdateUsuarioSchema(CamelModel):
    name: str
    email: str
    password: str
