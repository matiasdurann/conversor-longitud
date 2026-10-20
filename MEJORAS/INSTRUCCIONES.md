# Mantenimiento

Desde 1.3.0 la interfaz usa un tema oscuro con grises y acentos azules (incidencia #1). Al revisar cambios visuales, comprobar campos, menús desplegables, resultado, errores y tamaños mínimo/habitual; conservar la legibilidad y todas las acciones existentes.

## Flujo en GitHub

Reportar fallos mediante Issues. El propietario recibe avisos según su suscripción y los canales de notificación de GitHub. La IA debe reproducir el error, corregirlo en una rama y presentar una PR; matiasdurann hace la revisión e integración final. GitHub Actions ejecuta las pruebas en cada push/PR. CODEOWNERS indica el revisor, pero no impide por sí solo integrar: la protección obligatoria de main requiere configurar reglas en GitHub.

La publicación inicial está autorizada. No publicar audio, PDF, cachés ni credenciales. No está activa ninguna IA que escuche incidencias automáticamente solo por disponer de este workflow. Hace falta conectar y autorizar una integración compatible; mientras tanto, se puede pasar el enlace de la incidencia a la IA para preparar la corrección.

Actualización 1.2.1: tests/test_mejora.py prueba el intercambio en la interfaz real. Ejecutar `python -m unittest discover -s tests -v` y `python -m unittest -v test_conversor.py` en una sesión gráfica. Para probar solo lógica sin ventana: `python -m unittest -v tests.test_logica`. El intercambio muestra `—`, conserva literalmente la cantidad y no convierte hasta pulsar Convertir.

## Organización

Desde 1.2.0, `app.py` contiene la ventana CustomTkinter y VERSION; `logica.py` contiene las funciones independientes. `requirements.txt` declara la dependencia gráfica. `tests/test_logica.py` prueba la lógica sin interfaz; ejecutar `python -m unittest discover -s tests -v`. `Conversor.py` es ahora un acceso compatible, con la misma versión, y reexporta las funciones de lógica. Las referencias posteriores a la estructura inicial se conservan como contexto y deben interpretarse con esta actualización.

Para abrir: `python app.py` o `Iniciar.cmd`. Si falta CustomTkinter, instalar con `python -m pip install -r requirements.txt` únicamente tras autorización explícita. No instalar dependencias como parte de las pruebas de lógica. Para la regresión gráfica existente usar `python -m unittest -v test_conversor.py` con la dependencia instalada y sesión gráfica disponible. En cada cambio mantener VERSION coherente en app.py, Conversor.py y VERSION.txt.

- `Conversor.py`: funciones de conversión y formato, constantes de unidades y versión, interfaz Tkinter y acciones.
- `test_conversor.py`: pruebas automatizadas de cálculo y controles reales de Tkinter.
- `Iniciar.cmd`: acceso para ejecutar en Windows con Python instalado.
- `LEEME.md`: instrucciones de uso y limitaciones de los documentos de origen.
- `MEJORAS/`: historial, ideas, estas instrucciones y número de versión.
- Audio y PDF: fuentes originales, conservar sin modificar.

## Aplicar una actualización

1. Leer el código y las pruebas existentes antes de editar. Trabajar directamente en el programa original y conservar las funciones vigentes.
2. Modificar solo lo necesario. Mantener separada la lógica matemática de las acciones visuales. No añadir dependencias ni cambiar de tecnología sin necesidad.
3. Mantener la validación de edición y la validación final: durante la escritura se permiten estados intermedios como un signo o un separador; no se convierten hasta que contienen cifras. Validar el contenido completo también al pegar. No usar float para las conversiones.
4. Ejecutar `python -m unittest -v test_conversor.py`. Deben pasar todas las pruebas, sin errores ni omisiones. Hace falta una sesión gráfica con Tkinter; un entorno aislado puede impedir cargar Tcl/Tk aunque la instalación sea correcta.
5. Abrir `Iniciar.cmd` y revisar tamaños de ventana, tabulación, Intro, Escape y Alt+I. Probar pegados válidos e inválidos, las nueve combinaciones, intercambio, limpieza y botones repetidos. La aplicación no debe necesitar red.
6. Registrar automáticamente como parte de cada nueva modificación la fecha, comportamiento y correcciones en `CAMBIOS.md`; actualizar las ideas y problemas pendientes y estas instrucciones si cambia la estructura.
7. Incrementar `VERSION.txt` y `VERSION` en `Conversor.py` conjuntamente: parche para correcciones, versión menor para funciones compatibles y mayor para cambios incompatibles.

No hay un actualizador ni descargas automáticas. Este procedimiento guía las futuras modificaciones del proyecto y su documentación.
