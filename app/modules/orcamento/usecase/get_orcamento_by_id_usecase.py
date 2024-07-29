from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.orcamento import schemas
from app.modules.orcamento.model import OrcamentoModel
from app.modules.orcamento.repository import OrcamentoRepository


class GetOrcamentoById:
    """
    Search for orcamento by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = OrcamentoRepository()
        self._pydantic_model = pydantic_model_creator(OrcamentoModel)

    async def validate(self):
        """
        Search and validate existing orcamento in the database by id
        :return: model orcamento
        """
        orcamento = await self._repository.get_or_none(id=self._id)

        if not orcamento:
            raise HTTPException(
                detail="Orcamento not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return orcamento

    async def execute(self) -> schemas.OrcamentoSchema:
        camiseta = await self.validate()
        pyd_model = await self._pydantic_model.from_tortoise_orm(camiseta)
        return schemas.OrcamentoSchema(**pyd_model.dict())
