from datetime import datetime

from fastapi_camelcase import CamelModel


class PedidosSchema(CamelModel):
    id: int
    status: str
    total_value: str

    created_at: datetime
    updated_at: datetime
    finished_at: datetime

    class Config:
        orm_mode = True
