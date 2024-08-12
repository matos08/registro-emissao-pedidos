from datetime import datetime

from fastapi_camelcase import CamelModel


class PinturaSchema(CamelModel):
    id: int
    img_url: str
    size_painting: int
    value_colors: float

    created_at: datetime
    updated_at: datetime

    # cor: Optional[CorSchema]

    class Config:
        orm_mode = True
