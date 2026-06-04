import streamlit as st

from constants import APP_TITLE
from database import init_db

from views import (
    auth_view,
    sidebar,
    dashboard_view,
    setup_view,
    subjects_view,
    schedule_view,
    evaluations_view,
    exercises_view,
    study_view,
    personal_goals_view,
    weekly_review_view,
    stats_view,
    semesters_view,
)

def main():

    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="OK",
        layout="wide"
    )

    init_db()

    if "user_id" not in st.session_state:
        auth_view()
        return

    user_id = int(st.session_state.user_id)

    page = sidebar(user_id)

    views = {
        "Dashboard": dashboard_view,
        "Configuración inicial": setup_view,
        "Asignaturas": subjects_view,
        "Horario": schedule_view,
        "Evaluaciones": evaluations_view,
        "Ejercicios": exercises_view,
        "Estudio y reflexión": study_view,
        "Metas personales": personal_goals_view,
        "Revisión semanal": weekly_review_view,
        "Estadísticas": stats_view,
        "Semestres": semesters_view,
    }

    views[page](user_id)


if __name__ == "__main__":
    main()
