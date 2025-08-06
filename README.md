PROJECT::

Conversational LLM Web App
📌 Objective:
Build a fully functional Conversational AI Web Application powered by Hugging Face Transformers and designed with Streamlit. The app should allow users to chat with an LLM (Large Language Model), similar to ChatGPT, and support a clean UI, chat history, model selection, and export functionality.
📂 Deliverables:
    ● app.py: Main Streamlit app with frontend and chat logic.
    ● test_inference.py: Backend utility for managing conversations with Hugging Face models.
    ● requirements.txt: All required libraries for installation.
Folder structure should follow: CopyEdit LLM_Playground/
├── app.py
├── test_inference.py
└── requirements.txt

✅ Functional Requirements:
1. LLM Integration
    ● Use huggingface_hub.InferenceClient to connect to the mistralai/Mistral-7B-Instruct-v0.2 model.
    ● Use token-based authentication (token hardcoded or securely managed).
    ● Construct and maintain chat history using messages = [{"role": ..., "content": ...}].
2. Conversational Flow
    ● User inputs a question in a text box.
    ● Assistant provides an AI-generated response from the selected model.
    ● The conversation history is preserved across multiple turns to simulate a true chat.
    ● Clear Chat button resets the session and history.
3. Streamlit UI
    ● Design a clean, responsive UI using Streamlit.
    ● Features to implement:
        ○ Input text box for user queries.
        ○ Model selection dropdown (mistralai/Mistral-7B-Instruct-v0.1 and v0.2).
        ○ Chat avatars (🧑 for user, 🤖 for AI).
        ○ Markdown-style message formatting.
        ○ Export button to download the full conversation as .txt.

4. Optional Enhancements (Bonus Marks)
    ● Add time/date stamp to chat turns.
    ● Allow switching between light/dark theme.
    ● Add animated typing indicator using st.spinner.
🧪 Sample UI Behavior:
    yaml
    CopyEdit
🧠 LLM Playground
    💬 You: What is the capital of France?
    🤖 Bot: The capital of France is Paris.
    💬 You: What’s famous about it?
    🤖 Bot: Paris is known for the Eiffel Tower, cafes, fashion, and rich history.
🧰 Tech Stack:
    ● Python 3.10+
    ● Streamlit
    ● Hugging Face Transformers
    ● huggingface_hub, textwrap
📦 Installation Steps:
    streamlit run app.py