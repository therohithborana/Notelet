from fastapi import FastAPI, Request
from routes.note import note 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="NoteLet",
    description="A modern note-taking application built with FastAPI",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and templates configuration
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Include the note router
app.include_router(note, prefix="")

# Root redirect
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": []})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

