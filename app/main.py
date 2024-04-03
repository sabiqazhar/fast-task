from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes import task, user, auth
# from app.Model import models
# from database import engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(task.router, tags=['Task'], prefix='/api/task')
app.include_router(user.router, tags=['User'], prefix='/api/user')
app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')

@app.get("/api/test")
def root():
    return {"message": "testerterterter"}