from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.cliente import schemas
from app.modules.cliente.model import ClienteModel
from app.modules.cliente.repository import ClienteRepository


class UpdateClienteById:
    """
    Create for a cliente by id in the database
    """

    def __init__(self, id: int, payload: schemas.UpdateClienteSchema):
        self._id = id
        self._payload = payload
        self._repository = ClienteRepository()
        self._pydantic_model = pydantic_model_creator(ClienteModel)

    async def validate(self):
        """
        Search and validate existing cliente in the database by id
        :return: model cliente
        """
        cliente = await self._repository.get_or_none(id=self._id)

        if not cliente:
            raise HTTPException(
                detail="Cliente not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return cliente

    async def execute(self) -> schemas.ClienteSchema:
        await self.validate()
        cliente = await self._repository.update(self._id, **self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(cliente)
        return schemas.ClienteSchema(**pyd_model.dict())
