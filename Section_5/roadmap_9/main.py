import json
import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from api import greencity_api1
from views import index1

api = fastapi.FastAPI()
templates = Jinja2Templates('templates')


def load_env():
    with open('settings.json') as f:
        env = json.load(f)
    return env


def configure():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(greencity_api1.router2)
    api.include_router(index1.router1)
    env = load_env()
    print('setting >', env['setting'])
    print('warning >', env['warning'])


if __name__ == "__main__":
    configure()
    print('one')
    uvicorn.run('main:api', port=9000, host='127.0.0.1', reload=True)
else:
    configure()
    print('two')
