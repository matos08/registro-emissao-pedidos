from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel

from app.modules.orcamento.schemas import OrcamentoSchema
from app.modules.pintura.schemas import PinturaSchema


class CamisetaSchema(CamelModel):
    id: int
    size_shirt: str
    type_cloth: str
    type_shirt: str
    color_cloth: str

    created_at: datetime
    updated_at: datetime

    orcamento: Optional[OrcamentoSchema]
    pintura: Optional[PinturaSchema]

    class Config:
        orm_mode = True
