from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.cliente import schemas, usecase

router = APIRouter()


@router.post(
    "/cliente/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ClienteSchema,
)
async def create_cliente(payload: schemas.CreateClienteSchema):
    result = await usecase.create_cliente_usecase.CreateClienteUseCase(payload).execute()
    return result


@router.get(
    "/cliente/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ClienteSchema,
)
async def get_cliente_by_id(id: int):
    result = await usecase.GetClienteById(id).execute()
    return result


@router.delete(
    "/cliente/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_cliente_by_id(id: int):
    result = await usecase.DeleteClienteById(id).execute()
    return result


@router.put(
    "/cliente/{id}",
    response_model=schemas.ClienteSchema,
    status_code=status.HTTP_200_OK,
)
async def update_cliente_by_id(id: int, payload: schemas.UpdateClienteSchema):
    result = await usecase.UpdateClienteById(id, payload).execute()
    return result
