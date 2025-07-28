import streamlit as st

st.set_page_config(page_title="Jeffco AI Assistant")

st.title("Ask JeffBot – Jefferson County AI Assistant")
st.markdown("This assistant helps citizens with county services and FAQs.")

# Load Q&A from file
def load_knowledge():
    qa_pairs = []
    with open("jeffco_knowledge_base.txt", "r", encoding='utf-8') as file:
        lines = file.readlines()
    question = ""
    for line in lines:
        if line.startswith("Q:"):
            question = line[2:].strip()
        elif line.startswith("A:"):
            answer = line[2:].strip()
            qa_pairs.append((question.lower(), answer))
    return qa_pairs

knowledge_base = load_knowledge()

# Dropdown for department (for future use or filtering)
dept = st.selectbox("Choose Department", ["General", "DMV", "Public Records", "Parks & Rec", "Housing"])

# User input
user_input = st.text_input("Ask your question:")

# Basic keyword matching
if user_input:
    user_input_lower = user_input.lower()
    answer_found = False

    for q, a in knowledge_base:
        if any(word in q for word in user_input_lower.split()):
            st.markdown("### JeffBot Says:")
            st.write(a)
            answer_found = True
            break
    
    if not answer_found:
        st.markdown("### JeffBot Says:")
        st.write("I'm sorry, I couldn't find an answer to that. Please visit jeffco.us for more information.")
