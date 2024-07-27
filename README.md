# RAG System

This project is a React frontend and FastAPI backend application that allows users to upload PDF files and query a backend server. The project uses Docker Compose to manage the multi-container setup.

## Project Structure

- **frontend**: Contains the React frontend application.
- **backend**: Contains the FastAPI backend application.
- **documents**: Directory for storing uploaded PDF documents.
- **docker-compose.yml**: Docker Compose file to manage multi-container setup.

## Technologies Used

- React
- FastAPI
- Docker Compose
- PostgreSQL
- LangChain
- ChromaDB

## How to Run

1. **Set up Environment Variables**
   - Ensure the `ANTHROPIC_API_KEY` is set in your environment.

2. **Build and Start the Containers**
   ```bash
   docker-compose up --build
   ```

