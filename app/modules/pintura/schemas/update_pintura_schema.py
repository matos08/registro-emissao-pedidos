from fastapi_camelcase import CamelModel


class UpdatePinturaSchema(CamelModel):
    img_url: str
    size_painting: int
    value_colors: float
