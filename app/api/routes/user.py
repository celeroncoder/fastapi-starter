from fastapi import APIRouter, Depends
from app.api.controllers.user_controller import create_user, get_user_by_id
from app.api.models.user_model import UserCreate, UserResponse

router = APIRouter()

# POST request to create a user
@router.post("/", response_model=UserResponse)
async def create_user_route(user: UserCreate):
    return await create_user(user)

# GET request to retrieve a user by ID
@router.get("/{user_id}", response_model=UserResponse)
async def get_user_route(user_id: int):
    return await get_user_by_id(user_id)
