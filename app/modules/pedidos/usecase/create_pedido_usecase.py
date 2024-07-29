from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.pedidos import schemas
from app.modules.pedidos.model import PedidosModel
from app.modules.pedidos.repository import PedidoRepository


class CreatePedidoUseCase:
    def __init__(self, payload: schemas.CreatePedidosSchema):
        self._payload = payload
        self._repository = PedidoRepository()
        self._pydantic_model = pydantic_model_creator(PedidosModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        pedido = await self._repository.get_or_none(
            status=self._payload.status, total_value=self._payload.total_value
        )
        if pedido:
            raise HTTPException(
                detail="Pedido already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.PedidosSchema:
        await self.validate()
        pedido = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(pedido)
        return schemas.PedidosSchema(**pyd_model.dict())
