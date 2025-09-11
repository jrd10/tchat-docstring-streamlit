import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime


st.set_page_config(page_title="Chat Docstring")


@st.cache_resource
def get_messages_store():
    return list()

messages = get_messages_store()
st_autorefresh(interval=2000, limit=None, key="chat", debounce=True)

st.title("Chat Docstring")


if "username" not in st.session_state:
    st.session_state.username = ""


if not st.session_state.username:
    username_input = st.text_input("Entrez votre pseudo : ")
    if st.button("Rejoindre") and username_input:
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
