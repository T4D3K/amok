from os import path, environ
from fastapi import APIRouter, Response, status
from starlette.requests import Request

from .. import ROOT_DIR
import sys
import json

from ..common import CALLS, get_call_key

try:
    FIXTURES_PATH = sys.argv[1]
except:
    FIXTURES_PATH = environ.get('FIXTURES_PATH', path.join(ROOT_DIR, 'fixtures'))

amok_router = APIRouter()


async def handle_default_response(response):
    response.status_code = status.HTTP_200_OK
    response.body = json.dumps({"msg": "default"}).encode("utf-8")
    return response


@amok_router.get('/{url_path:path}')
async def get(url_path, request: Request, response: Response):
    try:
        return await handle_req(url_path, request, response, 'GET')
    except:
        return await handle_default_response(response)


@amok_router.delete('/{url_path:path}')
async def delete(url_path, request: Request, response: Response):
    try:
        return await handle_req(url_path, request, response, 'DELETE')
    except:
        return await handle_default_response(response)


@amok_router.post('/{url_path:path}')
async def post(url_path, request: Request, response: Response):
    try:
        return await handle_req(url_path, request, response, 'POST')
    except:
        return await handle_default_response(response)


@amok_router.put('/{url_path:path}')
async def put(url_path, request: Request, response: Response):
    try:
        return await handle_req(url_path, request, response, 'PUT')
    except:
        return await handle_default_response(response)


@amok_router.patch('/{url_path:path}')
async def patch(url_path, request: Request, response: Response):
    try:
        return await handle_req(url_path, request, response, 'PATCH')
    except:
        return await handle_default_response(response)


async def handle_req(url_path, request, response, method):
    key = await get_call_key(method, request, url_path)
    CALLS[key] = CALLS.get(key, 0) + 1

    with open(path.join(FIXTURES_PATH, 'cfg.json'), 'r') as f:
        conf = json.loads(f.read())

    resp_model_file = path.join(FIXTURES_PATH,
                                conf.get(key, conf.get(f'{method};{url_path};404', conf.get(f'{method};404', None))))
    with open(resp_model_file, 'r') as f:
        resp_model = json.loads(f.read())
        await map_response(resp_model, response)
        if 'headers' in resp_model:
            for k, v in resp_model['headers']:
                response.headers[k] = v
        return response


async def map_response(resp_model, response):
    response.status_code = resp_model['status']
    cont = resp_model['content']
    if isinstance(cont, str):
        cont = cont.encode('utf-8')
    else:
        cont = json.dumps(cont).encode('utf-8')
    response.body = cont
    response.headers['content-type'] = resp_model['content_type']
