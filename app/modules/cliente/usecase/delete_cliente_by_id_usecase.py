from fastapi import HTTPException, status

from app.modules.cliente.repository import ClienteRepository
from app.modules.core.default_schema import DefaultSchema


class DeleteClienteById:
    """
    Delete for a cliente by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = ClienteRepository()

    async def validate(self):
        """
        Search and validate existing cliente in the database by id
        :return: model cliente
        """
        cliente = await self._repository.get_or_none(id=self._id)

        if not cliente:
            raise HTTPException(
                detail="Cliente not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return cliente

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Cliente deleted successfully")
