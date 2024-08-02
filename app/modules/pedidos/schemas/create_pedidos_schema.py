from fastapi_camelcase import CamelModel


class CreatePedidosSchema(CamelModel):
    status: str
    total_value: float
    cliente_id: int
