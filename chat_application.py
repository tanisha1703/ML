
#impo goole api key ad streamlit
import streamlit as st
import google.generativeai as genai

# Gemini API configuration
genai.configure(api_key="AIzaSyA0FzQ-5w5oS3wlu5Agidv7GumIIe2VKq8")

#  GenerativeModel instance
model = genai.GenerativeModel('gemini-pro')

# Streamlit app title
st.title("Welcome to Chat AI")

# Create a text input for the user's question
text = st.text_input("Enter Your Question or Prombt:")

# Initialize the chat model
chat = model.start_chat(history=[])

# Create a button to generate the response
if st.button('Generate'):
    if text: 

        response = chat.send_message(text)
        st.write(response.text)  # Display the response
    else:
        st.write("Please enter a question before generating a response.")
