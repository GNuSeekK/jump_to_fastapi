from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto') # 암호화 하여 저장

def create_user(db: Session, user_create: UserCreate):
    db_user = User(
        username=user_create.username,
        password=pwd_context.hash(user_create.password1),
        email=user_create.email
    )
    db.add(db_user)
    db.commit()

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()