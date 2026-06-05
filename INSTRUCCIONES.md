# Instrucciones para usar y modificar la app

## Archivos principales

- `app.py`: contiene toda la aplicación.
- `requirements.txt`: lista las dependencias necesarias.
- `.streamlit/config.toml`: define colores y tema visual.
- `organizador.db`: se crea automáticamente cuando la app se usa. Aquí se guardan los datos.

## Cómo ejecutar la app

1. Abre una terminal en la carpeta del proyecto.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Inicia la app:

```bash
streamlit run app.py
```

## Cómo se guardan los datos

La app guarda los datos en una base SQLite llamada `organizador.db`.

Cada vez que el usuario crea cuenta, agrega asignaturas, evaluaciones, horarios, sesiones de estudio, metas o revisiones, la información queda guardada en esa base de datos.

Importante: si subes la app a un servidor gratuito o a Streamlit Cloud, la base local puede no ser permanente si el servidor se reinicia o redepliega. Para uso personal en tu computador, sí queda guardada mientras no borres `organizador.db`.

La app incluye un botón en la barra lateral para descargar un respaldo de los datos.

## Cómo cambiar textos

Busca en `app.py` el texto que quieres cambiar y reemplázalo.

Ejemplos:

- Título principal:

```python
APP_TITLE = "Organizador académico y personal"
```

- Opciones del menú:

```python
"Dashboard",
"Configuración inicial",
"Asignaturas",
```

- Mensajes al usuario:

```python
st.success("Perfil guardado.")
st.warning("Primero agrega una asignatura.")
```

## Cómo cambiar colores

Los colores principales están en dos lugares.

En `app.py`, dentro del bloque `<style>`:

```css
--bg: #f5f7f2;
--primary: #2f6f73;
--primary-dark: #24575b;
--accent: #c76d4d;
```

En `.streamlit/config.toml`:

```toml
primaryColor = "#2f6f73"
backgroundColor = "#f5f7f2"
secondaryBackgroundColor = "#ffffff"
textColor = "#26312d"
```

Si cambias un color, intenta cambiarlo en ambos lugares para mantener coherencia visual.

## Cómo agregar una nueva sección

1. Crea una función nueva en `app.py`, por ejemplo:

```python
def nueva_seccion_view(user_id: int) -> None:
    st.header("Nueva sección")
    st.write("Contenido de la sección.")
```

2. Agrega el nombre al menú en la función `sidebar`.

3. Agrega la función al diccionario `views` dentro de `main`.

```python
views = {
    "Nueva sección": nueva_seccion_view,
}
```

## Cómo cambiar la base de datos

Las tablas se crean en la función `init_db`.

Si quieres guardar un dato nuevo, normalmente necesitas:

1. Agregar una columna o tabla en `init_db`.
2. Agregar el campo visual con `st.text_input`, `st.number_input`, `st.selectbox`, etc.
3. Guardar el valor con una consulta `INSERT` o `UPDATE`.
4. Mostrar el valor donde corresponda.

Antes de cambiar la base, descarga un respaldo desde la app.

## Recomendación para GitHub

Sube estos archivos:

- `app.py`
- `requirements.txt`
- `README.md`
- `.streamlit/config.toml`
- `.gitignore`

No subas `organizador.db` si contiene datos reales de usuarios.
