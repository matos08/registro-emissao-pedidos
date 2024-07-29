from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.usuario import schemas
from app.modules.usuario.model import UsuarioModel
from app.modules.usuario.repository import UsuarioRepository


class CreateUsuarioUseCase:
    def __init__(self, payload: schemas.CreateUsuarioSchema):
        self._payload = payload
        self._repository = UsuarioRepository()
        self._pydantic_model = pydantic_model_creator(UsuarioModel)

    async def validate(self):
        """
        Checks if there is already a record in the database with the same name and gender values
        :return: None
        """
        usuario = await self._repository.get_or_none(
            name=self._payload.name, email=self._payload.email
        )
        if usuario:
            raise HTTPException(
                detail="Usuario already exist",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def execute(self) -> schemas.UsuarioSchema:
        await self.validate()
        usuario = await self._repository.create(self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(usuario)
        return schemas.UsuarioSchema(**pyd_model.dict())
