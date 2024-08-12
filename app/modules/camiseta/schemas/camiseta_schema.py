from datetime import datetime
from typing import Optional, List

from fastapi_camelcase import CamelModel

from app.modules.pintura.schemas import PinturaSchema


class CamisetaSchema(CamelModel):
    id: int
    size_shirt: str
    type_cloth: str
    type_shirt: str
    color_cloth: str
    quantity: int

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AddCamisetaPinturasSchema(CamelModel):
    camisete_id: int
    pinturas: List[int]


class CamisetaPinturasSchema(CamisetaSchema):
    pintura: Optional[PinturaSchema]
