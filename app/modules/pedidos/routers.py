from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.pedidos import schemas, usecase

router = APIRouter()


@router.post(
    "/pedido/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PedidosSchema,
)
async def create_pedido(payload: schemas.CreatePedidosSchema):
    result = await usecase.create_pedido_usecase.CreatePedidoUseCase(payload).execute()
    return result


@router.get(
    "/pedido/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.PedidosSchema,
)
async def get_pedido_by_id(id: int):
    result = await usecase.GetPedidoById(id).execute()
    return result


@router.delete(
    "/pedido/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_pedido_by_id(id: int):
    result = await usecase.DeletePedidoById(id).execute()
    return result


@router.put(
    "/pedido/{id}",
    response_model=schemas.PedidosSchema,
    status_code=status.HTTP_200_OK,
)
async def update_pedido_by_id(id: int, payload: schemas.UpdatePedidosSchema):
    result = await usecase.UpdatePedidoById(id, payload).execute()
    return result
