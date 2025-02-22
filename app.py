import base64
import glob
import os
import random

import rootpath
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from pydantic import Field, BaseModel

from core.chatgpt import llm_stream, llm_strict, process_stream, llm_chat
from core.history import History
from core.util import json_read_file

assistant_image_path = os.path.join(rootpath.detect(), "data", "images", "profile2.png").replace("\\", "/")
if os.path.exists(assistant_image_path):
    avatars = {"assistant": assistant_image_path,
               "user": "👤"}
else:
    avatars = {"assistant": "🤖",
               "user": "👤"}


class TalkingPointsModel(BaseModel):
    sustainable_fashion_question: bool = Field(...,
                                               description="The users question is related to the topic of sustainable fashion.")


def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string


# TODO redo parameters to make a class to extract the data or interface to simplify the parameters
def show_background():
    path = os.path.join(rootpath.detect(), "data", "images", "background.png").replace("\\", "/")
    if not os.path.exists(path):
        return
    # Load the Gaia image (for background)
    background_image = load_image(path)

    # Custom CSS to set the background image to the right and 50% of the width
    st.markdown(f"""
            <style>
            /* Set the background image on the right side taking up 50% width */
            .stApp {{
                background-image: url("data:image/png;base64,{background_image}");
                background-size: 100% auto; /* 50% of the width, auto for height */
                background-position: center center; /* Centered vertically, right-aligned */
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            /* Hide background image on smaller screens (e.g., below 768px) */
            @media (max-width: 650px) {{
                .stApp {{
                    background-image: none; /* Remove the background image */
                }}
            }}
            </style>
            """, unsafe_allow_html=True)


def display_messages():
    for message in st.session_state.history.logs:
        if message["role"] == "system":
            continue

        with st.chat_message(message["role"], avatar=avatars[message["role"]]):
            st.markdown(message["content"])


def streaming_logo_interface(company_name):
    st.title(company_name)
    show_background()

    display_messages()

    user_prompt = st.chat_input()  # Input box for the user

    if user_prompt is not None:
        st.session_state.history.user(user_prompt)

        with st.chat_message("user", avatar=avatars["user"]):
            st.markdown(user_prompt)

        with st.spinner("..."):
            response_stream = llm_stream(st.session_state.history)

        answers = process_stream(response_stream)
        assistant_message_placeholder = st.chat_message("assistant", avatar=avatars["assistant"])
        assistant_text = assistant_message_placeholder.empty()

        chunk = ""
        for chunk in answers:
            assistant_text.markdown(chunk)  # Update progressively
        st.session_state.history.assistant(chunk)  # Save final message in history


def read_pages(folder):
    paths = os.path.join(folder, "*.txt")
    pages = []
    for path in glob.glob(paths):
        loader = TextLoader(path, encoding="utf-8")
        pages.extend(loader.load_and_split())
    return pages


if __name__ == "__main__":

    if "history" not in st.session_state:
        data = json_read_file(os.path.join(rootpath.detect(), "data", "youtube", "lecture.json"))
        st.session_state.history = History()
        st.session_state.history.system("Lecture about Grant writing: " + data["response"]["text"])
        st.session_state.history.system("You are a Lecture helper, you help by answering any and all questions related to Grant writing, and give the user answers relating to the lecture that is part of this conversation:")
        st.session_state.history.system("Please introduce yourself to the user.")
        st.session_state.history.assistant("Hello! I'm here to assist you with any questions or information you might need related to grant writing. Whether you're looking for tips on finding grants, understanding the types of grants available, or need guidance on the application process, feel free to ask!")
    streaming_logo_interface("The Grantmanship Center")
