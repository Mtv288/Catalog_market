from  fastapi import APIRouter, Request
from app.core.templates import Jinja2Templates

router =APIRouter(
    prefix="",
    tags=["Главная"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "База"
        }
    )

@router.get("/mens")
def mens(request: Request):
    return templates.TemplateResponse(
        "mens.html",
        {
            "request": request,
            "title": "Муская обувь"
        }
    )