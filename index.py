## Thank to @gabigb117 de Docstring
## Video session of Sept. 11, 2025
## Create a chat appli with Streamlit - https://github.com/jrd10/tchat-docstring-streamlit/edit/main/index.py

import streamlit as st
from streamlit_autorefresh import st_autorefresh
from datetime import datetime


st.set_page_config(page_title="My first chat application with Streamlit")

## Pour stocker les messages
@st.cache_resource
def get_messages_store():
    return list()

## Rafraîchissement pour affichage des échanges tous les 2 ms, sans limite de temps
messages = get_messages_store()
st_autorefresh(interval=2000, limit=None, key="chat", debounce=True)

## Un petit peu de textes et un bouton pour le fun !
st.title("My first chat appli with Streamlit")
st.text("With the Gabigab117's contribution")

## Accéder au déploiement de ce code sur Streamlit
st.link_button("Accès au code sur Github", "https://github.com/jrd10/tchat-docstring-streamlit/blob/main/index.py")

## --- L'appli chat

## Vérifier si l'on est déjà connecté
if "username" not in st.session_state:
    st.session_state.username = ""

## si pas connecté (première visite ou rechargement de la page), entrer son pseudo 
if not st.session_state.username:
    username_input = st.text_input(" 👉 Entrez votre pseudo : ", placeholder="Hello from Docstring...")
    
# Original code: if st.button("Rejoindre") and username_input:
# Enter key not activate, only the button    
# C'est le « système », que nous avons défini, qui répond.
    if st.button("Touche Entrée ou ce bouton pour nous rejoindre :).") or username_input:
        st.session_state.username = username_input
        messages.append(
            {
                "author": "Système",
                "text": f" 🚨 {username_input} - a rejoint !",
                "time": datetime.now().strftime("%H:%M:%S")
            }
        )

        ## Rafraîchissement immédiat du message
        st.rerun()

## Message d'un nouvel utilisateur connecté
else:
    st.success(f" 🚨 {st.session_state.username} est connecté")

## Retourne les messages    
    for msg in messages:
        with st.chat_message(msg["author"]):
            st.markdown(f"*{msg["time"]}* - {msg["text"]}")

## Entrer son message    
    input_chat = st.chat_input("👉 Message...")

    ## Si la textbox est vide, pas d'envoi de message
    ## sinon, touche entrée ou le bouton à droite de la textbox
    if input_chat:
        messages.append({
            "author": st.session_state.username,
            "text": input_chat,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        
        ## Rafraîchissement immédiat du message
        st.rerun()
