from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.responses import JSONResponse

from schema.schema import DataResponse
from utils.LaptopExpertSystem import LaptopExpertSystem

app = FastAPI()

templates = Jinja2Templates(directory="templates")

expert_system = LaptopExpertSystem(10000)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {"request": request, "title": "Lab_1_SHI"}
    return templates.TemplateResponse("index.html", {"request": request, **context})


@app.post("/submit/")
async def submit_data(data: DataResponse):
    # print(data)

    laptop_data = {
        'usage': data.work,
        'budget': data.price,
        'specs': {
            'screen_size': str(data.screen) + ' inches',
            'weight': data.weight
        },
        'brand': data.brand
    }
    laptop = expert_system.recommend_laptop(laptop_data)
    print(laptop)
    return JSONResponse(content={"laptop": laptop})

