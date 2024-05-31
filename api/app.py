import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]= "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"

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description  = "A simple API server"
)

prompt = ChatPromptTemplate.from_template("Write me an essay on {topic} in 100 words")

llm = Ollama(model="llama2")
add_routes(
    app,
    prompt|llm,
    path="/essay"

)


if __name__=="__main__":
    uvicorn.run(app, host = "localhost", port = 8000)


