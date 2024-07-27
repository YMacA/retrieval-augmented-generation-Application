from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.llms import Anthropic
from langchain_community.document_loaders import PyPDFLoader
from io import BytesIO
from config import Config
import io
from PyPDF2 import PdfReader


class RAGSystem:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=Config.EMBEDDINGS_MODEL)
        self.vector_store = Chroma(persist_directory=Config.CHROMA_DB_DIR, embedding_function=self.embeddings)
        self.llm = Anthropic(temperature=0, anthropic_api_key=Config.ANTHROPIC_API_KEY)
        self.qa_chain = RetrievalQA.from_chain_type(self.llm, retriever=self.vector_store.as_retriever())

    def process_document_inutil(self, content, metadata):
        pdf_file = io.BytesIO(content)
        loader = PyPDFLoader(pdf_file)
        pages = loader.load()
        text = "\n".join([page.page_content for page in pages])
        text_splitter = CharacterTextSplitter(chunk_size=Config.CHUNK_SIZE, chunk_overlap=Config.CHUNK_OVERLAP)
        texts = text_splitter.split_text(text)
        self.vector_store.add_texts(texts, metadatas=[metadata] * len(texts))

    def process_document(self, content: bytes, metadata: dict):
        pdf_file = BytesIO(content)
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        text_splitter = CharacterTextSplitter(chunk_size=Config.CHUNK_SIZE, chunk_overlap=Config.CHUNK_OVERLAP)
        texts = text_splitter.split_text(text)
        self.vector_store.add_texts(texts, metadatas=[metadata] * len(texts))

    def query(self, question):
        return self.qa_chain.run(question)