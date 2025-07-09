from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Environment variables for LangChain (optional if you don't use LangSmith)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# FastAPI app setup
app = FastAPI(
    title="Langchain Server with Ollama",
    version="1.0",
    description="API using LangChain + Ollama LLaMA3"
)

# Load Ollama model
llm = Ollama(model="llama3")

# Define prompts
prompt_essay = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt_poem = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words.")

# Add routes using prompt + model
add_routes(app, prompt_essay | llm, path="/essay")
add_routes(app, prompt_poem | llm, path="/poem")

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
