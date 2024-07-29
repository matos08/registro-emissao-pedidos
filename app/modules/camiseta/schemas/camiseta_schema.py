from datetime import datetime

from fastapi_camelcase import CamelModel


class CamisetaSchema(CamelModel):
    id: int
    size_shirt: str
    type_cloth: str
    color_cloth: str

    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
