from fastapi import HTTPException, status

from app.modules.pedidos.repository import PedidoRepository
from app.modules.core.default_schema import DefaultSchema


class DeletePedidoById:
    """
    Delete for a pedido by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = PedidoRepository()

    async def validate(self):
        """
        Search and validate existing pedido in the database by id
        :return: model pedido
        """
        pedido = await self._repository.get_or_none(id=self._id)

        if not pedido:
            raise HTTPException(
                detail="Pedido not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return pedido

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Pedido deleted successfully")
