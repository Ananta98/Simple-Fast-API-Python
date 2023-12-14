from fastapi import Depends, APIRouter, HTTPException, status
from schemas.notes import Note
from database import notes_database
from utils.deps import get_current_user

noteRouter = APIRouter()

@noteRouter.get("/notes")
async def get_all_notes(user = Depends(get_current_user)):
    result = notes_database.get_all_notes(user_id=user["id"])
    return result

@noteRouter.post("/notes")
async def add_new_note(note : Note, user = Depends(get_current_user)):
    notes_database.insert_new_note(user["id"], note)
    return {'message' : 'Success add new note'}

@noteRouter.get("/notes/{note_id}")
async def get_single_note(note_id : str, user = Depends(get_current_user)):
    result = notes_database.get_single_note(note_id=note_id)
    return result

@noteRouter.put("/notes/{note_id}")
async def update_note(note_id : str, note : Note, user = Depends(get_current_user)):
    note_check = notes_database.get_single_note(note_id=note_id)
    if note_check is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Note doesn't exist"
        )
    notes_database.update_note(note_id=note_id, title=note.title, content=note.note)
    return {'message' : 'Success update note'}

@noteRouter.delete("/notes/{note_id}")
async def delete_note(note_id : str, user = Depends(get_current_user)):
    note_check = notes_database.get_single_note(note_id=note_id)
    if note_check is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Note doesn't exist"
        )
    notes_database.delete_note(note_id=note_id)
    return {'message' : 'Success delete note'}