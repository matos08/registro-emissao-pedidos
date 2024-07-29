from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.camiseta import schemas, usecase

router = APIRouter()


@router.post(
    "/camiseta/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CamisetaSchema,
)
async def create_camiseta(payload: schemas.CreateCamisetaSchema):
    result = await usecase.create_camiseta_usecase.CreateCamisetaUseCase(payload).execute()
    return result


@router.get(
    "/camiseta/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.CamisetaSchema,
)
async def get_camiseta_by_id(id: int):
    result = await usecase.GetCamisetaById(id).execute()
    return result


@router.delete(
    "/camiseta/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_camiseta_by_id(id: int):
    result = await usecase.DeleteCamisetaById(id).execute()
    return result


@router.put(
    "/camiseta/{id}",
    response_model=schemas.CamisetaSchema,
    status_code=status.HTTP_200_OK,
)
async def update_camiseta_by_id(id: int, payload: schemas.UpdateCamisetaSchema):
    result = await usecase.UpdateCamisetaById(id, payload).execute()
    return result
