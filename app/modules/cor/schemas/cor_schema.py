from datetime import datetime

from fastapi_camelcase import CamelModel


class CorSchema(CamelModel):
    id: int
    name: str
    value: float

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
