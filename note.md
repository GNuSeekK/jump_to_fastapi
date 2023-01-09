* 가상 환경 만들기
python -m venv ㅁㅁㅁㅁㅁ

* svelte 설치
npm create vite@latest frontend -- --template svelte
cd frontend
npm install
npm install moment : 시간 관련 처리 라이브러리

* svelte 실행 => npm run dev

* 테이블
pip install alembic # 설치
alembic init migrations # 초기화

alembic revision --autogenerate # 리비전 파일 만들기(변경 시에도 동일)
alembic upgrade head # 리비전 파일 새걸로 변경

* fastapi 실행
python -m uvicorn main:app --reload