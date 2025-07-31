import streamlit as st 
import os
import getpass
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage


st.markdown("Assalomu alaykum, sizga qanday yordam bera olaman!")
try:
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = st.text_input("Google Gemini uchun API kalitni kiriting", type="password")
    model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
    st.success("Model bilan aloqa o'rnatildi")
except Exception as ex:
    st.error(ex)

messages = st.container(height=200)

if prompt := st.chat_input("So'rang"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"TozalovchiAI: {model.invoke([HumanMessage(content=prompt)]).content}")