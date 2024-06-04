from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st

load_dotenv()

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text


st.set_page_config(page_title="Gemini_Demo")

st.header('Q&A bot')

input = st.text_input("Input: ",key='input')
submit = st.button('Ask the question')

if submit:
    response = get_gemini_response(input)
    st.subheader('Response')
    st.write(response)
