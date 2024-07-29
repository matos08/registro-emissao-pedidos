from datetime import datetime

from fastapi_camelcase import CamelModel


class ClienteSchema(CamelModel):
    id: int
    name: str
    email: str
    address: str
    telephone: str

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
