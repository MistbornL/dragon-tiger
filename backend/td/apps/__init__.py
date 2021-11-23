from fastapi import APIRouter
from td.apps.routers.game import router as user_router

router = APIRouter()
router.include_router(user_router)