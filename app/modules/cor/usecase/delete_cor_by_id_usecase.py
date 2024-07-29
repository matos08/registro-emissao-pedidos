from fastapi import HTTPException, status

from app.modules.cor.repository import CorRepository
from app.modules.core.default_schema import DefaultSchema


class DeleteCorById:
    """
    Delete for a cor by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = CorRepository()

    async def validate(self):
        """
        Search and validate existing cor in the database by id
        :return: model cor
        """
        cor = await self._repository.get_or_none(id=self._id)

        if not cor:
            raise HTTPException(
                detail="Cor not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return cor

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Cor deleted successfully")
