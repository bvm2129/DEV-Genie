# main_app.py
import streamlit as st
import huggingface_helper
import io

# Model options
model1 = "openai-community/gpt2"
model2 = "mistralai/Mistral-7B-Instruct-v0.1"

st.set_page_config(page_title="Dev-Genie", layout="centered")
st.title("🤖 DEV-GENIE!!")
st.subheader("Your AI assistant powered by Hugging Face models!")

# Sidebar – Model selection
selected_bot = st.sidebar.selectbox("Select a bot", (model1, model2))

# Sidebar – Download chat
if "chat_history" in st.session_state and st.sidebar.button("📥 Download Chat as .txt"):
    chat_text = ""
    for msg in st.session_state.chat_history:
        role = "You" if msg["role"] == "user" else "Genie"
        chat_text += f"{role}: {msg['content']}\n\n"

    buffer = io.StringIO(chat_text)
    st.download_button(
        label="Download Chat Log",
        data=buffer.getvalue(),
        file_name="genie_chat.txt",
        mime="text/plain"
    )

# Sidebar – Clear chat
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Session state setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show past conversation
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Genie is thinking..."):
        ai_response = huggingface_helper.generate_response(user_input, selected_bot)

    if not ai_response:
        ai_response = "Hmm, I couldn't quite get that. Can you rephrase it for me?"

    st.chat_message("assistant").markdown(ai_response)
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

# Floating emoji decoration
st.markdown(f"""
    <style>
        body::after {{
            content: "🎵";
            position: fixed;
            bottom: 15px;
            right: 15px;
            font-size: 2rem;
            animation: float 2s infinite;
            cursor: pointer;
        }}
        @keyframes float {{
            0%   {{transform: translateY(0);}}
            50%  {{transform: translateY(-10px);}}
            100% {{transform: translateY(0);}}
        }}
    </style>
""", unsafe_allow_html=True)
