from fastapi import FastAPI, Request
from routes.note import note 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

# Include the note router at the root path
app.include_router(note, prefix="")

# Root redirect
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": []})

