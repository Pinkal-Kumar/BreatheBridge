import streamlit as st
from core.state import initialize_state
from core.history import save_conversation
from Agents.agents import *

st.title("🧘‍♀️ Voice Therapy Assistant")

# Language selection dropdown
languages = {
    "English": "English",
    "Hindi (हिन्दी)": "Hindi",
    "Spanish (Español)": "Spanish",
    "French (Français)": "French",
    "German (Deutsch)": "German"
}

selected_language = st.selectbox("🌐 Choose your language:", list(languages.keys()))
chosen_lang_code = languages[selected_language]

# Initialize state if not already
if "state" not in st.session_state:
    state = initialize_state()
    state["language"] = chosen_lang_code
    st.session_state.state = state

# Session button
if st.button("Start Session"):
    state = st.session_state.state
    state["language"] = chosen_lang_code  # Ensure language is stored

    state = greet_agent(state)
    state = intro_agent(state)

    for i in range(3):
        state = breathing_agent(state, i)

    state = reflection_agent(state)
    state = scoring_agent(state)
    state = goodbye_agent(state)

    save_conversation(state)
    st.session_state.state = state

    st.success("✅ Session Complete!")
    st.write(state)

