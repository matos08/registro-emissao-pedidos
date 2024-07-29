from fastapi import HTTPException, status

from app.modules.usuario.repository import UsuarioRepository
from app.modules.core.default_schema import DefaultSchema


class DeleteUsuarioById:
    """
    Delete usuario by id in the database
    """

    def __init__(self, id: int):
        self._id = id
        self._repository = UsuarioRepository()

    async def validate(self):
        """
        Search and validate existing usuario in the database by id
        :return: model usuario
        """
        usuario = await self._repository.get_or_none(id=self._id)

        if not usuario:
            raise HTTPException(
                detail="Usuario not found.", status_code=status.HTTP_404_NOT_FOUND
            )
        return usuario

    async def execute(self) -> DefaultSchema:
        await self.validate()
        await self._repository.delete(id=self._id)
        return DefaultSchema(detail="Usuario deleted successfully")
