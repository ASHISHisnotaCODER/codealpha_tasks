import streamlit as st
from chatbot import get_bot_response

# Must be the first Streamlit command
st.set_page_config(page_title="H E R M I T", page_icon="⚡", layout="centered")

# Custom CSS for glowing neon yellow/lime theme
st.markdown("""
<style>
    /* Glowing Title */
    h1 {
        color: #ccff00 !important;
        text-shadow: 0 0 5px #ccff00, 0 0 10px #ccff00, 0 0 20px #ccff00, 0 0 40px #aadd00;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Neon Chat input */
    .stChatInputContainer {
        border: 1px solid #ccff00 !important;
        box-shadow: 0 0 10px #ccff00, inset 0 0 5px #ccff00 !important;
        border-radius: 10px !important;
        background-color: #000000 !important;
    }

    /* General text coloring */
    p {
        font-size: 1.1rem;
        color: #e0e0e0;
    }
    
    /* Neon Subtitle/Text */
    .neon-text {
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        margin-bottom: 30px;
    }
    
    /* User message styling */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: rgba(204, 255, 0, 0.05);
        border: 1px solid rgba(204, 255, 0, 0.2);
        border-radius: 10px;
    }
    
    /* Assistant message styling */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("H E R M I T")
st.markdown('<p class="neon-text">Welcome! You can say <b>hello</b>, ask for a <b>joke</b>, <b>time</b>, or the <b>weather in [city]</b>.</p>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "SYSTEM ONLINE. AWAITING INPUT..."}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = "⚡" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("TRANSMIT MESSAGE..."):
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get bot response
    response = get_bot_response(prompt)
    
    # Display assistant response
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
