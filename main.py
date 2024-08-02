import streamlit as st

USERS = {
    "info": [
        {"user": "admin", "password": "admin"},
        {"user": "jane", "password": "doe"},
        {"user": "john", "password": "smith"}
    ]
}

st.markdown("""
    <style>
    .button-container {
        position: absolute;
        top: 16px;
        right: 16px;
        z-index: 1000;
    }
    .stButton button {
        height: 50px;
        width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'logged' not in st.session_state:
    st.session_state.logged = False
    st.switch_page('pages/login.py')


def logout():
    del st.session_state['logged']


# def go_to_form():
#     st.switch_page('pages/image_form.py')


st.title('McApp')


def logged_content():
    st.divider()
    st.title("Take part in our photographic competition!")
    st.write("Send your application: ")
    if st.button('Form'):
        st.switch_page('pages/image_form.py')
    st.divider()


if st.session_state.logged:
    st.button('Logout', on_click=logout)
    logged_content()
    if 'password' not in st.session_state:
        logged_user = "unknown"
    else:
        logged_user = st.session_state['password']
    st.write(f"You are logged as {logged_user}.")

# streamlit run D:\repos\playground\testingChallenge\main.py --client.showSidebarNavigation=False
