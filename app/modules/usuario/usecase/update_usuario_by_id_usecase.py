from fastapi import HTTPException, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.modules.usuario import schemas
from app.modules.usuario.model import UsuarioModel
from app.modules.usuario.repository import UsuarioRepository


class UpdateUsuarioById:
    """
    Create for usuario by id in the database
    """

    def __init__(self, id: int, payload: schemas.UpdateUsuarioSchema):
        self._id = id
        self._payload = payload
        self._repository = UsuarioRepository()
        self._pydantic_model = pydantic_model_creator(UsuarioModel)

    async def validate(self):
        """
        Search and validate existing usuario in the database by id
        :return: model usuario
        """
        usuario = await self._repository.get_or_none(id=self._id)

        if not usuario:
            raise HTTPException(
                detail="Usuario not found", status_code=status.HTTP_404_NOT_FOUND
            )
        return usuario

    async def execute(self) -> schemas.UsuarioSchema:
        await self.validate()
        usuario = await self._repository.update(self._id, **self._payload.dict())
        pyd_model = await self._pydantic_model.from_tortoise_orm(usuario)
        return schemas.UsuarioSchema(**pyd_model.dict())
