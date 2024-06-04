from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st
from PIL import Image

load_dotenv()

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_vision_response(input,image):
    if input:
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text



st.set_page_config(page_title='Image-Desciption')
st.header('Image Desciption Bot ')
input = st.text_input("Input: ",key='input')

uploaded_file = st.file_uploader('Choose an Image..', type=['jpg','jpeg','png'])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image',use_column_width=True)

    submit = st.button('Tell me about Image')

    if submit:
        response  = get_gemini_vision_response(input,image)
        
        st.subheader('About:')
        st.write(response)


