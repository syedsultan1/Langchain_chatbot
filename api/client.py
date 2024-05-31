import requests
import streamlit as st

def get_llm_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json = {'input':{'topic':input_text}}
                             )
    return response.json()['output']

st.title("Langchain Demo With Llama2")
input_text = st.text_input("Give me a topic for essay")

if input_text:
    st.write(get_llm_response(input_text))