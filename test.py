from models import Question, Answer
from datetime import datetime
# q = Question(
#     subject='pybo가 무엇인가요?', 
#     content='pybo에 대해서 알고 싶습니다.', 
#     create_date=datetime.now()
#     )

# from database import SessionLocal
# db = SessionLocal()
# db.add(q)
# db.commit()

q = Question(
    subject='FastAPI 모델 질문입니다.', 
    content='id는 자동으로 생성되나요?', 
    create_date=datetime.now()
    )

from database import SessionLocal
db = SessionLocal()
db.add(q)
db.commit()