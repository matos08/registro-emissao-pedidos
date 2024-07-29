from fastapi_camelcase import CamelModel


class UpdateCamisetaSchema(CamelModel):
    size_shirt: str
    type_cloth: str
    color_cloth: str
