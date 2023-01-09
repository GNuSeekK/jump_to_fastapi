import datetime
from typing import Union
from pydantic import BaseModel, validator
from typing import List
from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

class Question(BaseModel):
    id: int
    subject: Union[str, None] = None # 3.10 부터는 object | None 으로 사용 가능
    content: str
    answers: List[Answer] = []
    create_date: datetime.datetime
    user: Union[User, None] = None # 3.10 부터는 object | None 으로 사용 가능
    modify_date: Union[datetime.datetime, None] = None
    voter: List[User] = []
    
    
    class Config:
        orm_mode = True

class QuestionList(BaseModel):
    total: int = 0
    question_list: List[Question] = []
    
class QuestionCreate(BaseModel):
    subject: str
    content: str
    
    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class QuestionUpdate(QuestionCreate):
    question_id: int
    
class QuestionDelete(BaseModel):
    question_id: int

class QuestionVote(BaseModel):
    question_id: int