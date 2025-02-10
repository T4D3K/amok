from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

from amok.common import CALLS, get_call_key

calls_router = APIRouter()


@calls_router.get('/')
async def get_calls():
    return CALLS


@calls_router.get('/{url_path:path}')
async def has_call_get(url_path, request: Request, response: Response):
    query_params = request.query_params
    query_params_str = str(query_params)
    call_key = f'GET;{url_path};{query_params_str};'
    return CALLS.get(call_key, 0)


@calls_router.delete('/{url_path:path}')
async def has_call_delete(url_path, request: Request, response: Response):
    call_key = await get_call_key('DELETE', request, url_path)
    CALLS[call_key] = CALLS.get(call_key, 0) + 1
    return CALLS.get(call_key, 0)


@calls_router.post('/{url_path:path}')
async def has_call_post(url_path, request: Request, response: Response):
    call_key = await get_call_key('POST', request, url_path)
    return CALLS.get(call_key, 0)


@calls_router.put('/{url_path:path}')
async def has_call_put(url_path, request: Request, response: Response):
    call_key = await get_call_key('PUT', request, url_path)
    return CALLS.get(call_key, 0)


@calls_router.patch('/{url_path:path}')
async def has_call_patch(url_path, request: Request, response: Response):
    call_key = await get_call_key('PATCH', request, url_path)
    return CALLS.get(call_key, 0)
