import streamlit as st
from database import fetch_all


def diagnostic_view(user_id: int):
    st.title("Diagnóstico inicial")

    subjects = fetch_all(
        "SELECT * FROM subjects WHERE user_id = ?",
        (user_id,)
    )

    st.subheader("Asignaturas registradas")
    st.write(len(subjects))

    if not subjects:
        st.warning("No tienes asignaturas aún.")
        return

    total_sct = sum(float(s["sct"]) for s in subjects)

    st.subheader("Carga académica estimada")
    st.write(f"SCT total: {total_sct}")

    if total_sct == 0:
        st.info("Sin carga académica")
    elif total_sct < 20:
        st.info("Carga baja")
    elif total_sct < 40:
        st.warning("Carga media")
    else:
        st.error("Carga alta")
