from fastapi_camelcase import CamelModel


class CreateOrcamentoSchema(CamelModel):
    service: str
    value: float
    descount: float
