from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.cliente import schemas
from app.modules.cliente.model import ClienteModel
from app.modules.cliente.repository import ClienteRepository


class CreateClienteUseCase:
    def __init__(self, payload: schemas.CreateClienteSchema):
        self._payload = payload
        self._repository = ClienteRepository()
        self._pydantic_model = pydantic_model_creator(ClienteModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        cliente = await self._repository.get_or_none(
            name=self._payload.name, email=self._payload.email
        )
        if cliente:
            raise HTTPException(
                detail="Cliente already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.ClienteSchema:
        await self.validate()
        cliente = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(cliente)
        return schemas.ClienteSchema(**pyd_model.dict())
