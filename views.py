import sqlite3
import time

import streamlit as st

from constants import *
from auth import *
from database import *
from services import *
auth_view()
sidebar()
setup_view()
dashboard_view()
subjects_view()
schedule_view()
personal_goals_view()
weekly_review_view()
stats_view()
semesters_view()
