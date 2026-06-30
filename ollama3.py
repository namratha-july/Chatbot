##GEN AI with OLLAMA LLAMA3.2 with dynamic prompt with streamlit
#pip install streamlit ollama
import streamlit as stl
import ollama
#set page configurations
#set the bag color and title of the page
stl.backgroung_color ="#27C2F5"
stl.set_page_config(
    page_title="GEN AI with OLLAMA LLAMA3.2 with dynamic prompt with streamlit",
    page_icon=":robot:",
    layout="centered"
)
#set the title of the page
stl.title("GEN AI with OLLAMA LLAMA3.2 with dynamic prompt with streamlit")
#create the session state for messages
if "messages" not in stl.session_state:
    stl.session_state.messages=[]
#user provide the prompt text
user_text=stl.chat_input("Enter your prompt:",key="user_text")

for msg in stl.session_state.messages:
    with stl.chat_message(msg['role']):
        stl.markdown(msg['content'])

if user_text:
    stl.session_state.messages.append(
        {
            "role":"user",
            "content":user_text
        }
    )
    with stl.chat_message("user"):
        stl.markdown(user_text)
    Response_Data="" 
    Streams=ollama.chat(
        model="llama3.2",
        messages=stl.session_state.messages,
        stream=True)
    for sent in Streams:
        Response_Data += sent["message"]["content"]
    stl.session_state.messages.append(
        {
            "role":"assistant",
            "content":Response_Data
        }
    )
    with stl.chat_message("assistant"):
        stl.markdown(Response_Data)