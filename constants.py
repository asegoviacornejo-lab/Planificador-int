from pathlib import Path

APP_TITLE = "Organizador académico y personal"

DB_PATH = Path(__file__).with_name("organizador.db")

ENERGY_LEVELS = ["Alta", "Media", "Baja"]

EVALUATION_TYPES = [
    "Prueba",
    "Certamen",
    "Control",
    "Laboratorio",
    "Informe",
    "Tarea",
    "Examen",
    "Otro",
]

EVALUATION_STATES = [
    "Pendiente",
    "Rendida",
    "Reprogramada",
    "Cancelada",
]

EXERCISE_STATES = [
    "No realizado",
    "Realizado con dificultad",
    "Comprendido y resuelto",
]

ACTIVITY_TYPES = [
    "Fija",
    "Flexible",
]

DAYS = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo",
]
