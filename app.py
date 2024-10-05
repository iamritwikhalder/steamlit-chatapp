from imports import *

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

st.title("ChatApp")


def update_chat_state(query, response):
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


def chatbot(query):
    chatbot = ChatOpenAI(api_key=OPENAI_API_KEY)
    prompt = prompt_generator(query)
    response = chatbot.invoke(prompt).content
    return response

def prompt_generator(query):
    chat_history = st.session_state.chats
    template = "You are a polite and helpful assistant."

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            MessagesPlaceholder("history"),
            ("user", query)
        ]
    )

    result = prompt.invoke(
        {   
            "history": chat_history,
        }
    )

    return result

# configuring the states
if "chats" not in st.session_state:
    st.session_state.chats = []

# display old messages
for chat in st.session_state.chats:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# taking input from the end user
query = st.chat_input("Type your message here")

# processing the input
if query:
    # displaying the current input
    with st.chat_message("user"):
        st.write(query)

    response = chatbot(query)

    # displaying the current output
    with st.chat_message("ai"):
        st.write(response)

    # storing the messages in the state
    update_chat_state(query, response)