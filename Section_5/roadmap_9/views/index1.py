from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi import APIRouter

templates = Jinja2Templates('templates')

router1 = APIRouter()


@router1.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
