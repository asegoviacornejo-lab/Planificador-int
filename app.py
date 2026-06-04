from __future__ import annotations

import hashlib
import os
import sqlite3
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import streamlit as st


APP_TITLE = "Organizador académico y personal"
DB_PATH = Path(__file__).with_name("organizador.db")
ENERGY_LEVELS = ["Alta", "Media", "Baja"]
