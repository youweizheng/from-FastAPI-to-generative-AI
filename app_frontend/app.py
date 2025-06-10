import streamlit as st
import requests

# Set page config
st.set_page_config(
    page_title="Cuisine Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("From FastAPI to GenAI Part 05: Cuisine Chatbot")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Get response from API
        response = requests.get(f"http://127.0.0.1:8008/chat?query={prompt}")
        if response.status_code == 200:
            answer = response.json()
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(answer)
        else:
            st.error("Failed to get response from the API")
    except Exception as e:
        st.error(f"An error occurred: {e}") 