from fastapi import FastAPI, Depends
from .schemas import UserReturn, AudioRequest, AudioResponseURL
from sqlalchemy.orm import Session
from .database import get_db
from .models import User, Audiofile

app = FastAPI()


@app.post("/create_user/")
def create_user(username: str, db: Session = Depends(get_db)) -> UserReturn | None:
    if db.query(User).filter(User.username == username):
        return None
    to_create = User(username=username)
    db.add(to_create)
    db.commit()
    return UserReturn(id=to_create.id, uuid=to_create.uuid)


@app.post("/create_audio")
def create_audio(data: AudioRequest, db: Session = Depends(get_db)) -> AudioResponseURL:
    return "https://mysite.com/"
