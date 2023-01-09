import datetime
from pydantic import BaseModel, validator
from domain.user.user_schema import User
from typing import Union, List

class AnswerCreate(BaseModel):
    content: str
    
    @validator('content') # 빈칸 허용 안하기 위한 조치
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
    user: Union[User, None] = None
    question_id: int
    modify_date: Union[datetime.datetime, None] = None
    voter: List[User] = []
    
    class Config:
        orm_mode = True
# 스키마 쓰는 이유
# http 프로토콜의 Body 입력 값은 Pydantic 스키마로 읽고
# http 프로토콜의 url에 포함된 입력값(url parameter)은 라우터의 스키마가 아니라 매개변수로 읽어야한다

class AnswerUpdate(AnswerCreate):
    answer_id: int
    
class AnswerDelete(BaseModel):
    answer_id: int
    
class AnswerVote(BaseModel):
    answer_id: int