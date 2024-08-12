from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.orcamento import schemas
from app.modules.orcamento.model import OrcamentoModel
from app.modules.orcamento.repository import OrcamentoRepository


class CreateOrcamentoUseCase:
    def __init__(self, payload: schemas.CreateOrcamentoSchema):
        self._payload = payload
        self._repository = OrcamentoRepository()
        self._pydantic_model = pydantic_model_creator(OrcamentoModel)

    async def validate(self):
        """Checks if there is already a record in the database with the same name and gender values
        :return: None"""

        orcamento = await self._repository.get_or_none(
            service=self._payload.service, value=self._payload.value,

        )
        if orcamento:
            raise HTTPException(
                detail="Orcamento already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.OrcamentoSchema:
        await self.validate()
        orcamento = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(orcamento)
        return schemas.OrcamentoSchema(**pyd_model.dict())
