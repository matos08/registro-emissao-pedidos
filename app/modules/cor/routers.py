from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.cor import schemas, usecase

router = APIRouter()


@router.post(
    "/cor/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CorSchema,
)
async def create_cor(payload: schemas.CreateCorSchema):
    result = await usecase.create_cor_usecase.CreateCorUseCase(payload).execute()
    return result


@router.get(
    "/cor/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.CorSchema,
)
async def get_cor_by_id(id: int):
    result = await usecase.GetCorById(id).execute()
    return result


@router.delete(
    "/cor/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_cliente_by_id(id: int):
    result = await usecase.DeleteCorById(id).execute()
    return result


@router.put(
    "/cor/{id}",
    response_model=schemas.CorSchema,
    status_code=status.HTTP_200_OK,
)
async def update_cor_by_id(id: int, payload: schemas.UpdateCorSchema):
    result = await usecase.UpdateCorById(id, payload).execute()
    return result
