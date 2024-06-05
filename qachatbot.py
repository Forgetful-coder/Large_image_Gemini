from dotenv import load_dotenv
import streamlit as st
import  google.generativeai as genai
import os

#Loading the api_key
load_dotenv()
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

#Setting up the model and chat_history
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(input):
    response = chat.send_message(input,stream=True)
    return response

#Setting up the front-end
st.set_page_config(page_title='Q&A demo')

st.header('Gemini LLM application')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input('Input: ',key='input')
submit = st.button('Ask the question')

# Getting respnse
if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(('You',input))
    st.subheader('The Response is')
    # Streaming the response
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader('The Chat History is')

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
