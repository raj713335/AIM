import os
import json
import cv2
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi import UploadFile, File
from starlette import status
from config.database import SessionLocal
from schemas.gen_ai_Schema import gen_ai_Schema
from ..auth import get_user_info
from schemas.userPayload import userPayload

from gen_ai.graph_explainer import graph_explainer

from llama_index.core import StorageContext, ServiceContext, load_index_from_storage
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

router = APIRouter(
    prefix='/genai',
    tags=['Generative AI']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.on_event("startup")
async def factory():
    global query_engine
    storage_context = StorageContext.from_defaults(persist_dir="data/POC/RAG/storage_mini")

    embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    llm = Groq(model="llama3-70b-8192", api_key=GROQ_API_KEY)

    service_context = ServiceContext.from_defaults(
        embed_model=embed_model,
        llm=llm
    )

    index = load_index_from_storage(storage_context, service_context=service_context)

    query_engine = index.as_chat_engine(service_context=service_context)


@router.post('/image_explainer', status_code=status.HTTP_200_OK)
async def image_explainer(file: UploadFile = File()):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')

        data = await file.read()
        file_name = f"{os.path.splitext(file.filename)[0]}{os.path.splitext(file.filename)[1]}"
        # Create a file path with the media folder
        file_path = f"static/dumps/{file_name}"
        # Save the file to the folder
        with open(file_path, "wb") as buffer:
            buffer.write(data)

        resp = graph_explainer(file_path)

        response = {"message": resp}

        return Response(json.dumps(response), media_type="application/json")
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)


@router.post('/chat_bot', status_code=status.HTTP_200_OK)
async def chat_bot(message_data: gen_ai_Schema):
    try:

        resp = query_engine.chat(message_data.message)

        response = {"message": resp.response}

        return Response(json.dumps(response), media_type="application/json")
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
