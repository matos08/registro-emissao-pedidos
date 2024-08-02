from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel

from app.modules.cor.schemas import CorSchema
from app.modules.orcamento.schemas import OrcamentoSchema


class PinturaSchema(CamelModel):
    id: int
    img_url: str
    size_painting: int
    value_colors: float

    created_at: datetime
    updated_at: datetime

    orcamento: Optional[OrcamentoSchema]
    cor: Optional[CorSchema]

    class Config:
        orm_mode = True
