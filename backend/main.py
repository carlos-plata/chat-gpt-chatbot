#   uvicorn main:app
#   uvicorn main:app --reload

#   Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    print("hello")
    return {"message": "Hello World"}