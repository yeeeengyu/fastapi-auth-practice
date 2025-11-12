from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.reqs import Request

app = FastAPI()
TEMPLATES = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/register", response_class=HTMLResponse)
def register():
    return FileResponse("templates/register.html")

@app.get("/login")
def login():
    return FileResponse("templates/login.html")

@app.get("/mypage")
def mypage():
    return FileResponse("templates/checkpage.html")

@app.post("/register/check")
async def registercheck(request: Request):
    pass # 여기서부터 짜면댈듯