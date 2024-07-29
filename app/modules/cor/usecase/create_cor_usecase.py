from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.cor import schemas
from app.modules.cor.model import CorModel
from app.modules.cor.repository import CorRepository


class CreateCorUseCase:
    def __init__(self, payload: schemas.CreateCorSchema):
        self._payload = payload
        self._repository = CorRepository()
        self._pydantic_model = pydantic_model_creator(CorModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        cor = await self._repository.get_or_none(
            name=self._payload.name, value=self._payload.value
        )
        if cor:
            raise HTTPException(
                detail="Cor already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.CorSchema:
        await self.validate()
        cor = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(cor)
        return schemas.CorSchema(**pyd_model.dict())
