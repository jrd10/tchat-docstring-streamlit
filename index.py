## Thank to @gabigb117 de Docstring
## Video session of Sept. 11, 2025
## Create a chat appli with Streamlit - 

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime


st.set_page_config(page_title="Chat Docstring")


@st.cache_resource
def get_messages_store():
    return list()

messages = get_messages_store()
st_autorefresh(interval=2000, limit=None, key="chat", debounce=True)

st.title("My first chat appli with Streamlit")
st.text("With the Gabigab117's contribution")

if "username" not in st.session_state:
    st.session_state.username = ""


if not st.session_state.username:
    username_input = st.text_input("Entrez votre pseudo : ", placeholder="Hello from Docstring...", icon=":material/thumb_up:")
        
    
# Original code: if st.button("Rejoindre") and username_input:
# Enter key not activate, only the button    
    if st.button("Rejoindre") or username_input:
        st.session_state.username = username_input
        messages.append(
            {
                "author": "Système",
                "text": f"{username_input} - a rejoint !",
                "time": datetime.now().strftime("%H:%M:%S")
            }
        )
        st.rerun()
else:
    st.success(f"{st.session_state.username} est connecté")
    
    for msg in messages:
        with st.chat_message(msg["author"]):
            st.markdown(f"*{msg["time"]}* - {msg["text"]}")
    
    input_chat = st.chat_input("Message...")
    if input_chat:
        messages.append({
            "author": st.session_state.username,
            "text": input_chat,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        st.rerun()
