from fastapi import FastAPI
from routes import authentication, notes

app = FastAPI()
app.include_router(authentication.authRouter)
app.include_router(notes.noteRouter)