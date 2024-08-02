import io
import time
from PIL import Image

import streamlit as st

clock = """
<script>
var span = document.getElementById('clock');

function time() {
  var d = new Date();
  var s = d.getSeconds()+37;
  var m = d.getMinutes()+19;
  var h = d.getHours()-2;
  span.textContent = 
    ("0" + h).substr(-2) + ":" + ("0" + m).substr(-2) + ":" + ("0" + s).substr(-2);
}

setInterval(time, 1000);

</script>
<body>
<span id="clock"></span>
</body>
"""

st.html(clock)

st.markdown("""
    <style>
    small {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Photograph contest application form")


def success():
    st.markdown(":green[Your application has been successfully submitted.]")
    time.sleep(1)
    st.balloons()


def failure(error_list):
    for e in error_list:
        st.divider()
        st.write(f":red[{e}]")


def validate():
    error_list = []
    if len(st.session_state.title) > 51:
        error_list.append("Title is too long.")
    if "." not in st.session_state.lat or -90.0 > float(st.session_state.lat) > 90 or len(st.session_state.lat) > 8:
        error_list.append("Latitude has wrong format.")
    if not st.session_state.name.isalpha():
        error_list.append("Wrong characters in name.")
    if "@" not in st.session_state.email:
        error_list.append("Wrong email address.")
    if st.session_state.uploader is not None:
        img = Image.open(io.BytesIO(st.session_state.uploader.getvalue()))
        width, height = img.size
        if height > 600:
            error_list.append("Height is too high.")
        if width >= 800:
            error_list.append("Width is too high.")

    if not error_list:
        success()
    else:
        failure(error_list)


with st.form('Application form', clear_on_submit=True):
    st.text_input('Title', key='title', placeholder="Up to 50 characters.")
    st.divider()
    st.write("Where photo have been taken:")
    st.write("Latitude format: 90.00000 to -90.00000")
    st.text_input('Latitude ', key='lat')
    st.write("Longtitude format: 180.00000 to -180.00000")
    st.text_input('Longtitude ', key='lon')
    st.divider()
    st.text_input('Name ', key='name')
    st.text_input('Surname ', key='surname')
    st.text_input('Email ', key='email')
    st.divider()
    st.write("Image should has JPEG extension, maximum size 800x600 and be below 500kB.")
    st.file_uploader('Image', type=['jpeg', 'jpg', 'png'], key='uploader', label_visibility="hidden")
    st.divider()
    st.form_submit_button('Send', on_click=validate)
