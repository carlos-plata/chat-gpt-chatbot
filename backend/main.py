#   uvicorn main:app
#   uvicorn main:app --reload

#   Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Function imports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_speech import convert_text_to_speech


# Initiate app
app = FastAPI()


# CORS - Origins
origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check Health
@app.get("/health")
async def check_health():
    return {"message": "Healthy."}

# Reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation reset."}


@app.post("/post-audio-get")
async def post_audio(file: UploadFile = File(...)):
    # Get saved audio
    # audio_input = open("voice.mp3", "rb")
    # Save file from FrontEnd
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input= open(file.filename, "rb")
    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)
    # Guard: ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio.")
    # Get chatgpt response
    chat_response = get_chat_response(message_decoded)
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get chat response.")
    # Store message
    store_messages(message_decoded, chat_response)
    # Convert chat response to audio
    audio_output=convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get Eleven Labs Audio Response.")
    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output
    # Return audio file
    return StreamingResponse(iterfile(),media_type="application/octet-stream")

# Post bot response
# Note: Browser not playing when using post request
#@app.post("/post-audio")
#async def post_audio(file: UploadFile = File(...)):
