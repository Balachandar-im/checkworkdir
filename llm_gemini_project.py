from http.client import responses

import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-2.5-pro')
def get_gemnin(question):
    response =  model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q/A Demo")

st.header('Gemini chatbot application')

input = st.text_input("Input : ",key = "input")
submit = st.button("Ask the question")

if submit:
    response = get_gemnin(input)
    st.subheader('The Response is : ')
    st.write(response)