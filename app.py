
import streamlit as st
from openai import OpenAI
import os

st.set_page_config(
    page_title="JARVIS AI",
    page_icon="🤖"
)

st.title("🤖 J.A.R.V.I.S")
st.caption("Your Personal AI Assistant")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("JARVIS API key is not configured.")
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Talk to JARVIS...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("JARVIS is thinking..."):
            try:
                response = client.responses.create(
                    model="gpt-5.5",
                    instructions=(
                        "You are JARVIS, an intelligent personal "
                        "AI assistant. Be friendly, helpful and polite."
                    ),
                    input=st.session_state.messages
                )

                answer = response.output_text
                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"JARVIS error: {e}")
