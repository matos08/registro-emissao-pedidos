from fastapi import APIRouter, status

from app.modules.core.default_schema import DefaultSchema
from app.modules.orcamento import schemas, usecase

router = APIRouter()


@router.post(
    "/orcamento/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.OrcamentoSchema,
)
async def create_orcamento(payload: schemas.CreateOrcamentoSchema):
    result = await usecase.create_orcamento_usecase.CreateOrcamentoUseCase(payload).execute()
    return result


@router.get(
    "/orcamento/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.OrcamentoSchema,
)
async def get_orcamento_by_id(id: int):
    result = await usecase.GetOrcamentoById(id).execute()
    return result


@router.delete(
    "/orcamento/{id}",
    response_model=DefaultSchema,
    status_code=status.HTTP_200_OK,
)
async def delete_orcamento_by_id(id: int):
    result = await usecase.DeleteOrcamentoById(id).execute()
    return result


@router.put(
    "/orcamento/{id}",
    response_model=schemas.OrcamentoSchema,
    status_code=status.HTTP_200_OK,
)
async def update_orcamento_by_id(id: int, payload: schemas.UpdateOrcamentoSchema):
    result = await usecase.UpdateOrcamentoById(id, payload).execute()
    return result
