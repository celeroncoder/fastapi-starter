from app.api.models.user_model import UserCreate, UserResponse
from app.services.user_service import create_user_in_db, get_user_from_db

async def create_user(user: UserCreate) -> UserResponse:
    created_user = await create_user_in_db(user)
    return UserResponse(id=created_user.id, username=created_user.username, email=created_user.email)

async def get_user_by_id(user_id: int) -> UserResponse:
    user = await get_user_from_db(user_id)
    return UserResponse(id=user["id"], username=user.username, email=user.email)
