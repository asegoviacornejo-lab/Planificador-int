import sqlite3

from constants import DB_PATH


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    with connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS profiles (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL DEFAULT '',
                university TEXT NOT NULL DEFAULT '',
                sct_hours REAL NOT NULL DEFAULT 27,
                usual_sleep REAL NOT NULL DEFAULT 7,
                needed_sleep REAL NOT NULL DEFAULT 8,
                energy_morning TEXT NOT NULL DEFAULT 'Media',
                energy_afternoon TEXT NOT NULL DEFAULT 'Media',
                energy_night TEXT NOT NULL DEFAULT 'Media',
                setup_complete INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS semesters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                semester_id INTEGER,
                name TEXT NOT NULL,
                sct REAL NOT NULL DEFAULT 0,
                theory_hours REAL NOT NULL DEFAULT 0,
                lab_hours REAL NOT NULL DEFAULT 0,
                target_grade REAL NOT NULL DEFAULT 5.0,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (semester_id) REFERENCES semesters(id) ON DELETE SET NULL
            );

            CREATE TABLE IF NOT EXISTS personal_responsibilities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                hours_week REAL NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS personal_goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                frequency TEXT NOT NULL,
                active INTEGER NOT NULL DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                date TEXT NOT NULL,
                weight REAL NOT NULL DEFAULT 0,
                state TEXT NOT NULL DEFAULT 'Pendiente',
                grade REAL,
                content TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS exercise_guides (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                total INTEGER NOT NULL DEFAULT 0,
                understood INTEGER NOT NULL DEFAULT 0,
                difficult INTEGER NOT NULL DEFAULT 0,
                pending INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                minutes INTEGER NOT NULL,
                method TEXT NOT NULL,
                session_date TEXT NOT NULL,
                productivity TEXT,
                comprehension TEXT,
                difficulty TEXT,
                concentration TEXT,
                notes TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                day TEXT NOT NULL,
                start_hour INTEGER NOT NULL,
                end_hour INTEGER NOT NULL,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS weekly_reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                review_date TEXT NOT NULL,
                went_well TEXT NOT NULL,
                difficult TEXT NOT NULL,
                improve TEXT NOT NULL,
                feeling TEXT NOT NULL,
                realistic TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
            """
        )


def fetch_all(query: str, params: tuple = ()):
    with connect() as conn:
        return conn.execute(query, params).fetchall()


def fetch_one(query: str, params: tuple = ()):
    with connect() as conn:
        return conn.execute(query, params).fetchone()


def execute(query: str, params: tuple = ()):
    with connect() as conn:
        conn.execute(query, params)

  
