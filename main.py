from fastapi import FastAPI, Request, Form
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from database import Database
from gpt_sql import GPTSQLGenerator
from chart_generator import ChartGenerator

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

gpt_sql_generator = GPTSQLGenerator()
database = Database()
chart_generator = ChartGenerator()

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def post_prompt(request: Request, prompt : str = Form(...)):
    try:
        sql = gpt_sql_generator.gerar_sql(prompt)
        df = database.consultar(sql)
        chart_path = chart_generator.generate_chart(df,"Resultado da Pesquisa")
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prompt": prompt,
            "sql": sql,
            "chart_path": chart_path
        })
    
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "prompt": prompt,
            "error": str(e)
        })