import streamlit as st

# Title and subtitle
st.set_page_config(page_title="JeffcoBot", layout="centered")
st.title("🤖 JeffcoBot – Your Jefferson County Assistant")
st.caption("Helping you navigate county services quickly and easily.")

# User input
user_input = st.text_input("Ask me something about Jefferson County:")

# Predefined Q&A dictionary
responses = {
    "senior services": "Jefferson County offers Meals on Wheels, senior transportation, and aging support. Visit jeffco.us/seniors.",
    "dmv": "You can renew your driver's license or plates through the Motor Vehicle office. Visit jeffco.us/MV for online services.",
    "property taxes": "You can pay or look up your property taxes at jeffco.us/assessor. Late fees may apply after April 30.",
    "trash": "Jeffco doesn’t provide trash pickup, but we support local recycling. Visit jeffco.us/recycling for drop-off options.",
    "volunteer": "Explore volunteer opportunities across departments at jeffco.us/volunteer.",
    "language": "For language access or translation assistance, contact Human Services at 303-271-1388.",
    "contact": "For general questions, call 303-271-6511 or visit jeffco.us/contact.",
    "court": "The Jefferson County Court is located in Golden, CO. Visit courts.state.co.us for court services.",
    "weather closure": "In case of weather-related office closures, updates are posted at jeffco.us and on Twitter @JeffcoColorado.",
    "human services": "Apply for SNAP, Medicaid, and more through the Human Services portal: jeffco.us/Human-Services."
}

# Process input
if user_input:
    found = False
    for keyword, reply in responses.items():
        if keyword in user_input.lower():
            st.success(reply)
            found = True
            break
    if not found:
        st.warning("Sorry, I’m still learning. Try asking about seniors, DMV, property tax, etc.")

# Footer
st.markdown("---")
st.caption("JeffcoBot is a demo project by Jigna Chaudhary for the Jefferson County Innovation Internship Interview.")
