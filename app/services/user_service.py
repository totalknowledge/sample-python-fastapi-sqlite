from typing import List, Optional
from sqlmodel import Session
from models.user import User, UserCreate, UserUpdate
from database import engine, create_db_and_tables
from fastapi import HTTPException

# Replace with actual hash if used in production
def hash_password(password: str) -> str:
    return "hashed_" + password

class UserService:
    def __init__(self):
        create_db_and_tables()

    def create_user(self, user_data: UserCreate) -> User:
        hashed_password = hash_password(user_data.password)
        new_user = User(**user_data.dict(), hashed_password=hashed_password)
        with Session(engine) as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
        return new_user

    def get_all_users(self) -> List[User]:
        with Session(engine) as session:
            return session.query(User).all()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        with Session(engine) as session:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        
    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        with Session(engine) as session:
            user = session.get(User, user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            if hasattr(user_update, 'password') and user_update.password is not None:
                user.hashed_password = hash_password(user_update.password)
                delattr(user_update, 'password')
            for var, value in user_update.dict(exclude_unset=True).items():
                setattr(user, var, value if value is not None else getattr(user, var))
            session.commit()
            session.refresh(user)
            return user

    def delete_user(self, user_id: int) -> bool:
        with Session(engine) as session:
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()
