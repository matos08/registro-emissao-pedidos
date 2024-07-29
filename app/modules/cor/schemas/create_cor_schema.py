from fastapi_camelcase import CamelModel


class CreateCorSchema(CamelModel):
    name: str
    value: float
