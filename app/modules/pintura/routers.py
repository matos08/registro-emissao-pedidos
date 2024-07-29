from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.pintura import schemas, usecase

router = APIRouter()


@router.post(
    "/pintura/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PinturaSchema,
)
async def create_pintura(payload: schemas.CreatePinturaSchema):
    result = await usecase.create_pintura_usecase.CreatePinturaUseCase(payload).execute()
    return result


@router.get(
    "/pintura/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.PinturaSchema,
)
async def get_pintura_by_id(id: int):
    result = await usecase.GetPinturaById(id).execute()
    return result


@router.delete(
    "/pintura/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_pintura_by_id(id: int):
    result = await usecase.DeletePinturaById(id).execute()
    return result


@router.put(
    "/pintura/{id}",
    response_model=schemas.PinturaSchema,
    status_code=status.HTTP_200_OK,
)
async def update_pintura_by_id(id: int, payload: schemas.UpdatePinturaSchema):
    result = await usecase.UpdatePinturaById(id, payload).execute()
    return result
