import streamlit as st
import cohere

# Sidebar for input
with st.sidebar:
    API_KEY = st.text_input("Cohere API Key", key="chatbot_api_key", type="password")
    st.markdown("[Get an Cohere API key](https://cohere.com/)")
    st.markdown("[Segment Documentation]( https://segment.com/docs/?ref=nav)")
    st.markdown("[mParticle Documentation]( https://docs.mparticle.com/)")
    st.markdown("[Lytics Documentation]( https://docs.lytics.com/)")
    st.markdown("[Zeotap Documentation](https://docs.zeotap.com/home/en-us/)")
    
    st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)")

    st.title("💬 Chatbot")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "CHATBOT", "message": "How can I help you?"}]

# Display chat history using st.write
for msg in st.session_state["messages"]:
    if msg["role"] == "CHATBOT":
        st.write(f"**Chatbot:** {msg['message']}")
    else:
        st.write(f"**You:** {msg['message']}")

# Handle user input
if prompt := st.text_input("Enter your message:"):
    if not API_KEY:
        st.info("Please add your Cohere AI API key to continue.")
        st.stop()

    client = cohere.Client(API_KEY)

    # Add user message to session state
    st.session_state["messages"].append({"role": "USER", "message": prompt})
    st.write(f"**You:** {prompt}")

    # Call Cohere API for response
    response = client.chat(chat_history=st.session_state["messages"], message=prompt)
    chatbot_message = response.text
    st.session_state["messages"].append({"role": "CHATBOT", "message": chatbot_message})
    st.write(f"**Chatbot:** {chatbot_message}")

