# import google.generativeai as genai
# import streamlit as st 

# st.title("Python Code analyzer")
# key='AIzaSyC9j5KaPVcanw9nvPAfKfORBqsCzBjx37I'
# genai.configure(api_key=key)
# system_instruction="""Take the python code as input and return corrected code with out any explanations,output and error explanation separating with sub headdings.Don't return the error explanation in the corrected code """



# model=genai.GenerativeModel(model_name='models/gemini-2.0-flash-thinking-exp-1219',system_instruction=system_instruction)

# import streamlit as st
# from streamlit_ace import st_ace

# prompt = st.text_area("Enter your code here :") 
# # st_ace(
# #     placeholder="Enter your code here...",
# #     language="python",
# #     theme="monokai",
# #     height=200
# # )



# if st.button('Analyze'):
#     result=model.generate_content(prompt).text
#     st.subheader("Corrected Code: ")
#     st.write(result)


import google.generativeai as genai
import streamlit as st

# Title of the Streamlit app
st.title("🐍 Python Code Analyzer")

# API key configuration
key = 'AIzaSyC9j5KaPVcanw9nvPAfKfORBqsCzBjx37I'
genai.configure(api_key=key)

# System instruction for the generative model
system_instruction = """Take the python code as input and return corrected code without any explanations. 
Output and error explanation separated with subheadings. Don't return the error explanation in the corrected code."""

# Initialize the generative model
model = genai.GenerativeModel(model_name='models/gemini-2.0-flash-thinking-exp-1219', system_instruction=system_instruction)

# Text area for code input
prompt = st.text_area("Enter your code here:")

# Analyze button
if st.button('Analyze'):
    result = model.generate_content(prompt).text
    st.subheader("Corrected Code:")
    st.write(result)
