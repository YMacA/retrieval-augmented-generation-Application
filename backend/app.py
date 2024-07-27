from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_system import RAGSystem
import shutil
import os
from fastapi.responses import JSONResponse
from io import BytesIO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

rag = RAGSystem()

UPLOAD_DIRECTORY = "uploaded_documents"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

class Question(BaseModel):
    text: str


@app.get("/")
async def read_root():
    return {"message": "Welcome to the RAG System API"}


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:        
        content = await file.read()
        metadata = {"filename": file.filename}
        rag.process_document(content, metadata)

        return {"info": f"File '{file.filename}' processed successfully"}

    except Exception as e:
        logger.error(f"Error processing file upload: {e}")        
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query(question: Question):
    try:
        response = rag.query(question.text)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=404, content={"message": "Not Found bro t"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)


        