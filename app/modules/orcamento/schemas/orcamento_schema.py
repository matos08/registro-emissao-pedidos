from datetime import datetime

from fastapi_camelcase import CamelModel


class OrcamentoSchema(CamelModel):
    id: int
    service: str
    value: float
    descount: float

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
