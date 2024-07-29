from fastapi_camelcase import CamelModel


class UpdateOrcamentoSchema(CamelModel):
    service: str
    value: float
    descount: float
