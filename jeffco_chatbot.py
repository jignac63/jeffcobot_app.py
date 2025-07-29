import streamlit as st

# Set up page
st.set_page_config(page_title="JeffcoBot", layout="centered")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Header and styling
st.markdown("""
    <style>
        body {
            background-color: #F9FAFC;
        }
        .user-msg {
            text-align: right;
            color: #002855;
            background-color: #e1efff;
            padding: 8px 12px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
        .bot-msg {
            text-align: left;
            color: #006400;
            background-color: #eaffea;
            padding: 8px 12px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 JeffcoBot – Your Jefferson County Assistant")
st.caption("Ask me anything about services like DMV, property taxes, volunteering, and more!")

# Define responses
responses = {
    "senior": "👵 Jefferson County offers Meals on Wheels, senior transportation, and aging support. Visit jeffco.us/seniors.",
    "dmv": "🚗 Renew your license or plates at jeffco.us/MV or visit Golden/Lakewood Motor Vehicle offices.",
    "property tax": "🏠 View and pay your property taxes at jeffco.us/assessor or call 303-271-8600.",
    "volunteer": "🙋‍♀️ Find volunteer roles at jeffco.us/volunteer across many departments.",
    "human services": "🧑‍⚕️ Get info on SNAP, Medicaid, and housing at jeffco.us/human-services.",
    "permits": "📄 Apply for building/zoning permits at planning.jeffco.us.",
    "parks": "🌳 Visit jeffco.us/open-space for parks, trails, and outdoor activities.",
    "language": "🌐 Translation support is available at 303-271-1388 via Human Services.",
    "jobs": "💼 Open roles are posted at jeffco.us/jobs.",
    "contact": "📞 Call 303-271-6511 or use jeffco.us/contact to reach departments.",
    "court": "⚖️ Jefferson County Courthouse is in Golden. More info at courts.state.co.us.",
    "closure": "🌨️ For emergency closures, check jeffco.us or follow @JeffcoColorado on Twitter."
}

# User input
user_input = st.text_input("💬 Ask your question here:")

# Process user input and generate bot reply
if user_input:
    response_found = None
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            response_found = response
            break
    if not response_found:
        response_found = "🤔 Sorry, I’m still learning. Try asking about DMV, taxes, or volunteering."

    # Append to chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response_found))

# Display conversation history
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div class='user-msg'>👤 You: {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>🤖 JeffcoBot: {msg}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("JeffcoBot is a demo project by Jigna Chaudhary for the Jefferson County Innovation Internship Interview.")
