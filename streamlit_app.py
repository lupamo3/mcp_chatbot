import streamlit as st
import requests

st.title("💬 Customer Support Chatbot")
question = st.text_input("Ask your question about a product (e.g., monitor):")

if question:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://localhost:8000/ask",  
                json={"question": question},
                timeout=10
            )
            response.raise_for_status()
            st.success("Response:")
            st.json(response.json())
        except requests.exceptions.RequestException as e:
            st.error(f"Backend error: {e}")
        except requests.exceptions.JSONDecodeError:
            st.error("Invalid JSON returned from backend.")
            st.text(f"Raw backend reply:\n{response.text}")
