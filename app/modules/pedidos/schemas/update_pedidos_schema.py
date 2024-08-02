from fastapi_camelcase import CamelModel


class UpdatePedidosSchema(CamelModel):
    status: str
    total_value: float
