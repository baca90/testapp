import time
import streamlit as st
from main import USERS

if 'logged' not in st.session_state:
    st.session_state.logged = False


def login():
    """Updates logged state if form submit is clicked."""
    for ui in USERS['info']:
        if ui['user'] == st.session_state.user and ui['password'] == st.session_state.password:
            st.session_state.logged = True
            st.session_state.password = st.session_state.password
            break
    if not st.session_state.logged:
        st.error('Incorrect email or password.')


# Show login form.
if not st.session_state.logged:
    with st.form('login form', clear_on_submit=True):
        st.text_input('User', key='user')
        st.text_input('Password', type="password", key='password')
        st.form_submit_button('Login', on_click=login)
else:
    time.sleep(0.1)  # make the page switch visible
    st.switch_page('main.py')
