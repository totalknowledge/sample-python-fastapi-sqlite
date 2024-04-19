from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from models.user import User, UserCreate, UserUpdate
from services.user_service import UserService

router = APIRouter()
def get_user_service():
    return UserService()

@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)

@router.get("/users/", response_model=List[User], status_code=status.HTTP_200_OK)
def read_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_all_users()

@router.get("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: UserUpdate, user_service: UserService = Depends(get_user_service)):
    updated_user = user_service.update_user(user_id, user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user_service.delete_user(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
