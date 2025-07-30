import streamlit as st

# Page setup
st.set_page_config(page_title="JeffcoBot", layout="centered")
st.title("🤖 JeffcoBot – Your Jefferson County Assistant")
st.caption("Helping you navigate county services quickly and easily.")

# User input
user_input = st.text_input("Ask me something about Jefferson County:")

# Flexible keyword map – using multiple keywords per topic
keywords_map = {
    "senior services": ["senior", "aging", "elder", "meals on wheels"],
    "dmv": ["dmv", "driver", "license", "plates", "vehicle"],
    "property taxes": ["tax", "property tax", "assessor", "pay tax"],
    "trash": ["trash", "garbage", "recycle", "compost"],
    "volunteer": ["volunteer", "help", "community service"],
    "language": ["translation", "language", "interpreter"],
    "contact": ["contact", "call", "phone", "support"],
    "court": ["court", "judge", "legal"],
    "closures": ["closure", "closed", "weather", "emergency"],
    "human services": ["snap", "medicaid", "benefits", "human services", "housing"],
    "permits": ["permit", "zoning", "building", "inspection"],
    "parks": ["park", "trails", "open space", "recreation"],
    "career": ["job", "career", "employment", "opening", "vacancy"]
}

# Response text
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

# Match logic
if user_input:
    matched = False
    lower_input = user_input.lower()
    for topic, keywords in keywords_map.items():
        if any(keyword in lower_input for keyword in keywords):
            st.success(responses[topic])
            matched = True
            break
    if not matched:
        st.warning("Sorry, I’m still learning. Try asking about taxes, DMV, senior services, or jobs in Jeffco.")

# Footer
st.markdown("---")
st.caption("JeffcoBot is a demo project by Jigna Chaudhary for the Jefferson County Innovation Internship Interview.")
