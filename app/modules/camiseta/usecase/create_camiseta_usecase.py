from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.camiseta import schemas
from app.modules.camiseta.model import CamisetaModel
from app.modules.camiseta.repository import CamisetaRepository


class CreateCamisetaUseCase:
    def __init__(self, payload: schemas.CreateCamisetaSchema):
        self._payload = payload
        self._repository = CamisetaRepository()
        self._pydantic_model = pydantic_model_creator(CamisetaModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        camiseta = await self._repository.get_or_none(
            size_shirt=self._payload.size_shirt, type_cloth=self._payload.type_cloth,
            color_cloth=self._payload.color_cloth
        )
        if camiseta:
            raise HTTPException(
                detail="Camiseta already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.CamisetaSchema:
        await self.validate()
        camiseta = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(camiseta)
        return schemas.CamisetaSchema(**pyd_model.dict())
