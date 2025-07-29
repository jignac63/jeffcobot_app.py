import streamlit as st

# Set page configuration
st.set_page_config(page_title="JeffcoBot", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #F9FAFC;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #002855;
        }
        .stTextInput>div>div>input {
            font-size: 18px;
        }
        .stCaption {
            color: #666;
        }
        .footer {
            font-size: 14px;
            color: #999999;
            text-align: center;
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Optional banner image
st.image("https://www.jeffco.us/ImageRepository/Document?documentID=26999", width=320, caption="Jefferson County Official")

# Title and intro
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("🤖 JeffcoBot – Your Jefferson County Assistant")
st.markdown("Ask me about local services like DMV, property taxes, volunteer programs, and more.")
st.markdown("---")

# User input
user_input = st.text_input("💬 What would you like to know?")

# Predefined Q&A dictionary
responses = {
    "senior services": "Jefferson County offers Meals on Wheels, senior transportation, and aging support. Visit jeffco.us/seniors.",
    "dmv": "You can renew your driver's license or plates at jeffco.us/MV or visit a local Motor Vehicle office in Golden or Lakewood.",
    "property taxes": "Look up or pay your property taxes online at jeffco.us/assessor. For help, call 303-271-8600.",
    "trash": "Jeffco doesn’t provide trash pickup but offers recycling and composting resources. Visit jeffco.us/recycling.",
    "volunteer": "To volunteer with Jeffco, check open opportunities at jeffco.us/volunteer. Roles are available across departments!",
    "language": "Need translation help? Jeffco Human Services offers interpretation and language access support: 303-271-1388.",
    "contact": "Call 303-271-6511 for general inquiries, or use the department directory at jeffco.us/contact.",
    "court": "Visit the Jefferson County Courthouse in Golden or go to courts.state.co.us for judicial services.",
    "closures": "For weather or emergency closures, check alerts on jeffco.us or follow @JeffcoColorado on Twitter.",
    "human services": "For SNAP, Medicaid, or housing help, go to jeffco.us/human-services or visit the Peak Chatbot.",
    "permits": "Building or zoning permits can be applied for at planning.jeffco.us. Online and in-person help available.",
    "parks": "Explore Jeffco Open Space parks and trails at jeffco.us/open-space. Great for hiking, biking, and family time!",
    "career": "Visit jeffco.us/jobs for current openings with Jefferson County Government."
}

# Response logic
if user_input:
    found = False
    for keyword, reply in responses.items():
        if keyword in user_input.lower():
            st.success(reply)
            found = True
            break
    if not found:
        st.warning("❗ I’m still learning. Try asking about DMV, taxes, volunteering, or senior services.")

# Footer
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div class='footer'>JeffcoBot is a demo project by Jigna Chaudhary for the Jefferson County Innovation Internship Interview.</div>", unsafe_allow_html=True)
