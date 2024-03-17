from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import elevenlabs
import os

# Set your API key
elevenlabs.set_key(os.environ.get("XI_LABS_API_KEY"))

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_audio")
async def generate_audio(request: Request):
    data = await request.form()
    text = data.get("text")
    audio_stream = elevenlabs.generate(text, stream=True)
    return StreamingResponse(audio_stream, media_type="audio/mpeg")