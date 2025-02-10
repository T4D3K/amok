from base64 import b64encode

CALLS = dict()


async def get_call_key(method, request, url_path):
    body = await request.body()
    b64 = b64encode(body).decode('utf-8')
    query_params = request.query_params
    query_params_str = str(query_params)
    log_key = f'{method};{url_path};{query_params_str};{b64}'
    return log_key
