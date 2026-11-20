
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="SkillBridge AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# App Title
st.title("🤖 SkillBridge AI Assistant")

st.subheader("Agentic RAG Powered Chatbot")

st.write(
    "Welcome! Ask questions about student records, "
    "academic performance, attendance, and institutional policies."
)

st.divider()

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
prompt = st.chat_input("Ask your question here...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.info("RAG pipeline integration is coming next!")

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "RAG pipeline integration is coming next!"
        }
    )
