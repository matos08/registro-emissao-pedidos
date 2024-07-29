from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.cor import schemas
from app.modules.cor.model import CorModel
from app.modules.cor.repository import CorRepository


class GetCorById:
    """
    Search for a cor by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = CorRepository()
        self._pydantic_model = pydantic_model_creator(CorModel)

    async def validate(self):
        """
        Search and validate existing cor in the database by id
        :return: model cor
        """
        cor = await self._repository.get_or_none(id=self._id)

        if not cor:
            raise HTTPException(
                detail="Cor not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return cor

    async def execute(self) -> schemas.CorSchema:
        cor = await self.validate()
        pyd_model = await self._pydantic_model.from_tortoise_orm(cor)
        return schemas.CorSchema(**pyd_model.dict())
