from fastapi import HTTPException, status

from app.modules.orcamento.repository import OrcamentoRepository
from app.modules.core.default_schema import DefaultSchema


class DeleteOrcamentoById:
    """
    Delete for orcamento by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = OrcamentoRepository()

    async def validate(self):
        """
        Search and validate existing orcamento in the database by id
        :return: model orcamento
        """
        orcamento = await self._repository.get_or_none(id=self._id)

        if not orcamento:
            raise HTTPException(
                detail="Orcamento not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return orcamento

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Orcamento deleted successfully")
