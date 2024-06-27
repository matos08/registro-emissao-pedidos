from fastapi import APIRouter

router = APIRouter()


@router.get("/health-check", description="Router to check application.")
async def health_check():
    return dict(detail="Application running")
