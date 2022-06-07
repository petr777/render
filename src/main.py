from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
from pydantic import BaseModel


BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory='templates')

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

class RequestQuery(BaseModel):
    lat: float
    lon: float

@api_router.get("/", status_code=200)
def root(request: Request):
    """
    Root GET
    """

    data = {
        'key': request.query_params.get('key'),
        'point': request.query_params.get('point'),
        'page': request.query_params.get('page'),
        'page_size': request.query_params.get('page_size'),
        'radius': request.query_params.get('radius'),
        'type': request.query_params.get('type'),
        'fields': request.query_params.get('fields')
    }

    return templates.TemplateResponse(
        'index.html',
        {'request': request, **data}
    )

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

