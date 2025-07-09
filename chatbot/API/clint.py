import requests
import streamlit as st

# Use only one input field
st.title('LangChain Demo with LLaMA3 via Ollama')
input_text = st.text_input("Enter a topic (for essay or poem):")

# Function to call essay endpoint
def get_essay_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/essay/invoke",
            json={"input": {"topic": input_text}}
        )
        return response.json().get('output', 'No output key found.')
    except Exception as e:
        return f"Error: {str(e)}"

# Function to call poem endpoint
def get_poem_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={"input": {"topic": input_text}}
        )
        return response.json().get('output', 'No output key found.')
    except Exception as e:
        return f"Error: {str(e)}"

# Show results when user enters something
if input_text:
    st.subheader("Essay:")
    st.write(get_essay_response(input_text))

    st.subheader("Poem:")
    st.write(get_poem_response(input_text))

    st.subheader("Both:")
    st.write(get_essay_response(input_text))
    st.write(get_poem_response(input_text))
