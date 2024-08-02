from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel

from app.modules.pedidos.schemas import PedidosSchema


class OrcamentoSchema(CamelModel):
    id: int
    service: str
    value: float
    descount: float

    created_at: datetime
    updated_at: datetime

    pedidos: Optional[PedidosSchema]

    class Config:
        orm_mode = True
