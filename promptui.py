from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
model="meta-llama/Llama-3.1-8B-Instruct",
task="text-generation",
)

model = ChatHuggingFace(llm=llm)

st.header("Reasearch Assistant")

user_input = st.text_input("Enter your prompt here")

if st.button("Summarize"):
    st.text("Generating...")
    response = model.invoke(user_input)
    st.write(response.content)