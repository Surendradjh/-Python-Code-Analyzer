import google.generativeai as genai
import streamlit as st
import os
st.title("🐍 Python Code Analyzer")

key = os.getenv("api_key")
genai.configure(api_key=key)

system_instruction = """Take the python code as input and return corrected code without any explanations. 
Output and error explanation separated with subheadings. Don't return the error explanation in the corrected code."""

model = genai.GenerativeModel(model_name='models/gemini-2.0-flash-thinking-exp-1219', system_instruction=system_instruction)

prompt = st.text_area("Enter your code here:")

if st.button('Analyze'):
    result = model.generate_content(prompt).text
    st.subheader("Corrected Code:")
    st.write(result)
