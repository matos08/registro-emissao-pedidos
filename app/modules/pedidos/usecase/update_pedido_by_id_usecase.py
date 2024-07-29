from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.pedidos import schemas
from app.modules.pedidos.model import PedidosModel
from app.modules.pedidos.repository import PedidoRepository


class UpdatePedidoById:
    """
    Create for a pedido by id in the database
    """

    def __init__(self, id: int, payload: schemas.UpdatePedidosSchema):
        self._id = id
        self._payload = payload
        self._repository = PedidoRepository()
        self._pydantic_model = pydantic_model_creator(PedidosModel)

    async def validate(self):
        """
        Search and validate existing pedido in the database by id
        :return: model pedido
        """
        pedido = await self._repository.get_or_none(id=self._id)

        if not pedido:
            raise HTTPException(
                detail="Pedido not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return pedido

    async def execute(self) -> schemas.PedidosSchema:
        await self.validate()
        pedido = await self._repository.update(self._id, **self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(pedido)
        return schemas.PedidosSchema(**pyd_model.dict())
