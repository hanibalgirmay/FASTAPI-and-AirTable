from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pathlib
import os
from functools import lru_cache 
from dotenv import load_dotenv
from .airtable import Airtable

@lru_cache()
def cached_dotenv():
    load_dotenv()

cached_dotenv()


AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY=os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME=os.environ.get("AIRTABLE_TABLE_NAME")


BASE_DIR = pathlib.Path(__file__).parent #src

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates")

@app.get('/')
def home_page(request: Request):
    return templates.TemplateResponse('home.html',{"request":request})

@app.post('/')
def home_signup(request:Request,userEmail:str = Form(...)):
    """
    TODO CSRF for security
    """
    #To be send to airtable
    client = Airtable(
        base_id = AIRTABLE_BASE_ID,
        api_key = AIRTABLE_API_KEY,
        table_name = AIRTABLE_TABLE_NAME
    )
      
    isSuccess = client.create_record({"user email":userEmail})
    return templates.TemplateResponse('home.html',{"request":request, "submited_email":userEmail, "isSuccess":isSuccess})