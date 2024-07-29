from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.pintura import schemas
from app.modules.pintura.model import PinturaModel
from app.modules.pintura.repository import PinturaRepository


class GetPinturaById:
    """
    Search for pintura by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = PinturaRepository()
        self._pydantic_model = pydantic_model_creator(PinturaModel)

    async def validate(self):
        """
        Search and validate existing pintura in the database by id
        :return: model pintura
        """
        pintura = await self._repository.get_or_none(id=self._id)

        if not pintura:
            raise HTTPException(
                detail="Pintura not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return pintura

    async def execute(self) -> schemas.PinturaSchema:
        pintura = await self.validate()
        pyd_model = await self._pydantic_model.from_tortoise_orm(pintura)
        return schemas.PinturaSchema(**pyd_model.dict())
