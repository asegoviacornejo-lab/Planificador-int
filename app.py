import streamlit as st
from database import init_db, fetch_all, execute
from views.diagnostic import diagnostic_view

init_db()

st.set_page_config(page_title="Planificador", layout="wide")

st.sidebar.title("Menú")
page = st.sidebar.radio("Ir a", ["Diagnóstico", "Inicializar datos"])

# 🔥 NUEVO: estado inicial
subjects = fetch_all("SELECT * FROM subjects")

if page == "Inicializar datos":
    st.title("Inicializar sistema")

    st.write("Esto crea datos base para que el sistema funcione.")

    if st.button("Crear ejemplo de asignaturas"):
        execute("INSERT INTO subjects (name, sct) VALUES (?, ?)", ("Cálculo III", 6))
        execute("INSERT INTO subjects (name, sct) VALUES (?, ?)", ("Física II", 5))
        execute("INSERT INTO subjects (name, sct) VALUES (?, ?)", ("Programación", 4))
        st.success("Datos creados")
        st.rerun()

if page == "Diagnóstico":
    diagnostic_view()
