from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.camiseta import schemas
from app.modules.camiseta.model import CamisetaModel
from app.modules.camiseta.repository import CamisetaRepository


class GetCamisetaById:
    """
    Search for a camiseta by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = CamisetaRepository()
        self._pydantic_model = pydantic_model_creator(CamisetaModel)

    async def validate(self):
        """
        Search and validate existing camiseta in the database by id
        :return: model camiseta
        """
        camiseta = await self._repository.get_or_none(id=self._id)

        if not camiseta:
            raise HTTPException(
                detail="Camiseta not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return camiseta

    async def execute(self) -> schemas.CamisetaSchema:
        camiseta = await self.validate()
        pyd_model = await self._pydantic_model.from_tortoise_orm(camiseta)
        return schemas.CamisetaSchema(**pyd_model.dict())
