from datetime import datetime


from fastapi_camelcase import CamelModel


class UsuarioSchema(CamelModel):
    id: int
    name: str
    email: str
    password: str

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
