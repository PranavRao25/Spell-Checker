import streamlit as st
from spell_checker import SpellChecker
from io import StringIO

st.title('Spell Checker')
st.text("Enter text and the bot will provide the correct spellings for misspelled ones")

sp = SpellChecker()
if 'messages' not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
    st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = sp.spellCheck(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


def reset_conversation():
    st.session_state.messages = []


st.button('Reset Chat', on_click=reset_conversation)
