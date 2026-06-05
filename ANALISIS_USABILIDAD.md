# Análisis de comodidad de uso

## Evaluación general

La app es cómoda para uso personal porque organiza la información en secciones claras: dashboard, configuración inicial, asignaturas, horario, evaluaciones, ejercicios, estudio, metas, revisión semanal, estadísticas y semestres.

La navegación lateral ayuda a mantener todo disponible sin obligar al usuario a recordar rutas o comandos. El diseño visual aplicado usa colores suaves, buen contraste, tarjetas discretas y botones consistentes, lo que hace que la experiencia se sienta más tranquila y ordenada.

## Puntos fuertes

- La estructura coincide con el flujo real de un estudiante: primero perfil y asignaturas, luego evaluaciones, estudio y revisión.
- Los formularios están agrupados por tema, lo que reduce confusión.
- Los datos se guardan en SQLite, así no se pierden al cerrar la página en uso local.
- El dashboard entrega una vista rápida de progreso, próxima evaluación y recomendación.
- La estética evita colores agresivos y mantiene una identidad visual sobria.
- Se agregó respaldo descargable de la base de datos desde la barra lateral.

## Cosas que ya son cómodas

- Menú lateral fijo.
- Botones de ancho completo en formularios importantes.
- Métricas visuales para resumen.
- Barras de progreso para configuración y ejercicios.
- Expansores para no saturar la pantalla con demasiada información.

## Riesgos de comodidad

- Hay muchas secciones en el menú lateral; para un usuario nuevo puede sentirse extenso.
- Algunas páginas tienen formularios largos.
- La eliminación de elementos es directa; sería mejor agregar confirmación antes de borrar asignaturas o actividades.
- En pantallas pequeñas, las tablas de horario pueden requerir desplazamiento horizontal.
- La app guarda datos localmente; si se despliega en una nube gratuita sin base externa, la persistencia no está garantizada a largo plazo.

## Mejoras recomendadas

- Agregar confirmación antes de eliminar datos.
- Separar el dashboard en bloques más visuales: urgencias, avance, descanso y próximos pasos.
- Agregar edición completa de asignaturas, evaluaciones y actividades, no solo eliminación o cambio parcial.
- Agregar exportación a Excel o CSV.
- Usar una base de datos externa si la app será usada por varias personas o estará publicada en internet.

## Conclusión

La app es coherente y cómoda para un organizador académico personal. Para uso local, guarda bien los datos y la experiencia visual es armónica. Para uso público o multiusuario, conviene conectar una base de datos externa y añadir confirmaciones antes de acciones destructivas.
