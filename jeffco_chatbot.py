
import streamlit as st
import openai

st.set_page_config(page_title="Jeffco AI Assistant")

st.title("Ask JeffBot – Jefferson County AI Assistant")
st.markdown("This assistant helps citizens with county services and FAQs.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Dropdown for department
dept = st.selectbox("Choose Department", ["General", "DMV", "Public Records", "Parks & Rec", "Housing"])

# User input
user_input = st.text_input("Ask your question:")

if user_input:
    prompt = f"You are a helpful assistant from the {dept} department of Jefferson County. Answer the following:\n{user_input}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}]
    )
    
    st.markdown("### JeffBot Says:")
    st.write(response['choices'][0]['message']['content'])
