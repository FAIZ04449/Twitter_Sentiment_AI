from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sentiment_model import analyze_sentiment

app = FastAPI(title="Twitter Sentiment Analysis AI")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Tweet(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
def analyze(tweet: Tweet):
    return analyze_sentiment(tweet.text)

