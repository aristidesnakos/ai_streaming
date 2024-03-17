from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config.env_var import OPENAI_API_KEY
from utils import *
from openai import AsyncOpenAI

VOICE_ID = '21m00Tcm4TlvDq8ikWAM'

aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_audio")
async def generate_audio(request: Request):
    print(f"Request headers: {request.headers}")
    print(f"Request body: {await request.body()}")
    data = await request.form()
    text = data.get("text")
    response = await aclient.chat.completions.create(model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': text}],
                                                     temperature=1, stream=True)
    async def text_iterator():
        async for chunk in response:
            delta = chunk.choices[0].delta
            yield delta.content

    audio_stream = await text_to_speech_input_streaming(VOICE_ID, text_iterator())
    return asyncio.run(audio_stream)