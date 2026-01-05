import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.rag_chain import get_rag_answer


st.set_page_config(
    page_title="Policy Assistant",
    layout="centered"
)

st.title("📘 Domain-Specific Policy Assistant")
st.caption("Answers are generated only from uploaded policy documents")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a question:")

if st.button("Ask") and user_input:
    answer = get_rag_answer(user_input)

    st.session_state.chat_history.append(
        ("You", user_input)
    )
    st.session_state.chat_history.append(
        ("Assistant", answer)
    )

for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")
