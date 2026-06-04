import streamlit as st
from asignaturas import mostrar_asignaturas
from calendario import mostrar_calendario

pagina = st.sidebar.radio(
    "Menú",
    ["Inicio", "Asignaturas", "Calendario"]
)

if pagina == "Inicio":
    st.title("Inicio")

elif pagina == "Asignaturas":
    mostrar_asignaturas()

elif pagina == "Calendario":
    mostrar_calendario()
