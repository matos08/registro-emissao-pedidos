from fastapi_camelcase import CamelModel


class CreateCamisetaSchema(CamelModel):
    size_shirt: str
    type_cloth: str
    color_cloth: str
