from fastapi import HTTPException, status

from app.modules.camiseta.repository import CamisetaRepository
from app.modules.core.default_schema import DefaultSchema


class DeleteCamisetaById:
    """
    Delete for a camiseta by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = CamisetaRepository()

    async def validate(self):
        """
        Search and validate existing camiseta in the database by id
        :return: model camiseta
        """
        camiseta = await self._repository.get_or_none(id=self._id)

        if not camiseta:
            raise HTTPException(
                detail="Camiseta not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return camiseta

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Camiseta deleted successfully")
