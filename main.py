from imports import *

import streamlit as st

st.title("ChatApp")


if "chats" not in st.session_state:
    st.session_state.chats = []

for chat in st.session_state.chats:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

query = st.chat_input("Type your message here")

if query:
    with st.chat_message("user"):
        st.write(query)

    response = "Chup BSDK!"

    with st.chat_message("ai"):
        st.write(response)

    user_input = {
        "role" : "user",
        "content" : query
    }

    ai_response = {
        "role" : "ai",
        "content" : response
    }

    st.session_state.chats.append(user_input)
    st.session_state.chats.append(ai_response)