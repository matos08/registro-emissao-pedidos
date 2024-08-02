from typing import Optional
from datetime import datetime

from fastapi_camelcase import CamelModel

from app.modules.cliente.schemas import ClienteSchema


class PedidosSchema(CamelModel):
    id: int
    status: str
    total_value: float

    created_at: datetime
    updated_at: datetime
    finished_at: datetime

    cliente: Optional[ClienteSchema]

    class Config:
        orm_mode = True
