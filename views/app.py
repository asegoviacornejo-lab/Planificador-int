import streamlit as st
from database import init_db
from auth import auth_view
from views.diagnostic import diagnostic_view

init_db()

st.set_page_config(page_title="Planificador", layout="wide")

if "user_id" not in st.session_state:
    auth_view()
    st.stop()

user_id = st.session_state.user_id

st.sidebar.title("Menú")
page = st.sidebar.radio("Ir a", ["Diagnóstico"])

if page == "Diagnóstico":
    diagnostic_view(user_id)
