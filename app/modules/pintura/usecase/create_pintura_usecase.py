from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.pintura import schemas
from app.modules.pintura.model import PinturaModel
from app.modules.pintura.repository import PinturaRepository


class CreatePinturaUseCase:
    def __init__(self, payload: schemas.CreatePinturaSchema):
        self._payload = payload
        self._repository = PinturaRepository()
        self._pydantic_model = pydantic_model_creator(PinturaModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        pintura = await self._repository.get_or_none(
            size_painting=self._payload.size_painting, value_colors=self._payload.value_colors,

        )
        if pintura:
            raise HTTPException(
                detail="Pintura already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.PinturaSchema:
        await self.validate()
        pintura = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(pintura)
        return schemas.PinturaSchema(**pyd_model.dict())
