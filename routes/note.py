from fastapi import APIRouter, Request
from models.note import Note
from config.db import conn
from fastapi.responses import HTMLResponse, RedirectResponse
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from bson import ObjectId

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    try:
        docs = conn.notes.notes.find({})
        newDocs = []
        for doc in docs:
            newDocs.append({
                "id": str(doc["_id"]),
                "title": doc.get("title", ""),
                "desc": doc.get("desc", ""),
                "important": doc.get("important", False)
            })
        return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})
    except Exception as e:
        print(f"Error: {str(e)}")
        return templates.TemplateResponse("index.html", {"request": request, "newDocs": [], "error": str(e)})

@note.get("/search", response_class=HTMLResponse)
async def search_notes(request: Request):
    try:
        query = request.query_params.get("q", "").strip()
        if query:
            # Search in both title and description using case-insensitive regex
            docs = conn.notes.notes.find({
                "$or": [
                    {"title": {"$regex": query, "$options": "i"}},
                    {"desc": {"$regex": query, "$options": "i"}}
                ]
            })
        else:
            docs = conn.notes.notes.find({})
        
        newDocs = []
        for doc in docs:
            newDocs.append({
                "id": str(doc["_id"]),
                "title": doc.get("title", ""),
                "desc": doc.get("desc", ""),
                "important": doc.get("important", False)
            })
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "newDocs": newDocs,
            "search_query": query
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "newDocs": [], 
            "error": str(e),
            "search_query": query
        })

@note.post("/")
async def create_item(request: Request):
    try:
        form_data = await request.form()
        form_dict = dict(form_data)
        form_dict["important"] = "important" in form_dict
        note = conn.notes.notes.insert_one(form_dict)
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        print(f"Error: {str(e)}")
        return templates.TemplateResponse("index.html", {"request": request, "newDocs": [], "error": str(e)})

@note.post("/delete/{id}")
async def delete_note(id: str):
    try:
        conn.notes.notes.delete_one({"_id": ObjectId(id)})
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        print(f"Error: {str(e)}")
        return RedirectResponse(url="/", status_code=303)

@note.get("/edit/{id}", response_class=HTMLResponse)
async def edit_note(request: Request, id: str):
    try:
        doc = conn.notes.notes.find_one({"_id": ObjectId(id)})
        if doc:
            note = {
                "id": str(doc["_id"]),
                "title": doc.get("title", ""),
                "desc": doc.get("desc", ""),
                "important": doc.get("important", False)
            }
            return templates.TemplateResponse("edit.html", {"request": request, "note": note})
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        print(f"Error: {str(e)}")
        return RedirectResponse(url="/", status_code=303)

@note.post("/update/{id}")
async def update_note(request: Request, id: str):
    try:
        form_data = await request.form()
        form_dict = dict(form_data)
        form_dict["important"] = "important" in form_dict
        conn.notes.notes.update_one(
            {"_id": ObjectId(id)},
            {"$set": form_dict}
        )
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        print(f"Error: {str(e)}")
        return RedirectResponse(url="/", status_code=303) 

