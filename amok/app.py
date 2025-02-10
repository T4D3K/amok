from fastapi import FastAPI
from .resources.fixtures_mock import amok_router
from .resources.calls import calls_router

app = FastAPI(title='Generic Mock')

app.include_router(amok_router, prefix='/api')
app.include_router(calls_router, prefix='/calls')
