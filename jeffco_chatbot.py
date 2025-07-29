import streamlit as st

# Page config
st.set_page_config(page_title="JeffcoBot", layout="centered")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.markdown("""
    <h1 style='text-align:center; color:#002855;'>🤖 JeffcoBot</h1>
    <h4 style='text-align:center;'>Your Friendly Jefferson County Assistant</h4>
    <p style='text-align:center; color:#666;'>Ask me about local services like DMV, property taxes, volunteering, parks, and more!</p>
    <hr>
""", unsafe_allow_html=True)

# Input box
user_input = st.text_input("💬 Ask a question", placeholder="e.g., How can I pay my property taxes?", key="input")

# Bot response dictionary
responses = {
    "senior": "👵 Jefferson County offers Meals on Wheels, senior transportation, and aging support. Visit jeffco.us/seniors.",
    "dmv": "🚗 You can renew your driver’s license or plates at jeffco.us/MV or at a Motor Vehicle office in Golden/Lakewood.",
    "property tax": "🏠 You can view and pay your property taxes at jeffco.us/assessor or call 303-271-8600.",
    "volunteer": "🙋‍♀️ Find volunteer opportunities at jeffco.us/volunteer. We'd love to have you involved!",
    "human services": "🧑‍⚕️ SNAP, Medicaid, and housing services info is at jeffco.us/human-services.",
    "permits": "📄 You can apply for zoning and building permits at planning.jeffco.us.",
    "parks": "🌲 Explore Open Space parks and trails at jeffco.us/open-space!",
    "language": "🌐 Language translation support is available at 303-271-1388 via Human Services.",
    "jobs": "💼 Check out jeffco.us/jobs for current openings at Jefferson County.",
    "contact": "📞 Call 303-271-6511 or visit jeffco.us/contact for more help.",
    "court": "⚖️ Courts are located in Golden. Visit courts.state.co.us for info.",
    "closure": "🌨️ Weather closures are posted at jeffco.us and @JeffcoColorado on Twitter."
}

# Handle input
if user_input:
    reply = None
    for keyword, response in responses.items():
        if keyword in user_input.lower():
            reply = response
            break
    if not reply:
        reply = "🤔 Sorry, I’m still learning. Try asking about DMV, property taxes, volunteering, or courts."

    # Add to chat history
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", reply))
    st.experimental_rerun()

# Show chat history
st.markdown("<div style='background-color:#f9f9f9; padding:1rem; border-radius:10px;'>", unsafe_allow_html=True)

for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div style='text-align:right; color:#002855;'><b>👤 You:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align:left; color:#006400;'><b>🤖 JeffcoBot:</b> {message}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("JeffcoBot is a demo project by Jigna Chaudhary for the Jefferson County Innovation Internship Interview.")
