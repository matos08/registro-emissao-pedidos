from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.usuario import schemas, usecase

router = APIRouter()


@router.post(
    "/usuario/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UsuarioSchema,
)
async def create_usuario(payload: schemas.CreateUsuarioSchema):
    result = await usecase.create_usuario_usecase.CreateUsuarioUseCase(payload).execute()
    return result


@router.get(
    "/usuario/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.UsuarioSchema,
)
async def get_usuario_by_id(id: int):
    result = await usecase.GetUsuarioById(id).execute()
    return result


@router.delete(
    "/usuario/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_usuario_by_id(id: int):
    result = await usecase.DeleteUsuarioById(id).execute()
    return result


@router.put(
    "/usuario/{id}",
    response_model=schemas.UsuarioSchema,
    status_code=status.HTTP_200_OK,
)
async def update_usuario_by_id(id: int, payload: schemas.UpdateUsuarioSchema):
    result = await usecase.UpdateUsuarioById(id, payload).execute()
    return result
