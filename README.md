# Conversor de longitud

Aplicación de escritorio en **Python y CustomTkinter** para convertir milímetros, centímetros y metros. Funciona sin Internet después de instalar las dependencias.

## Abrir la aplicación

Requiere Python 3 con Tkinter. Descarga o clona el repositorio y, desde su carpeta, ejecuta:

```console
python -m pip install -r requirements.txt
python app.py
```

En Windows también puedes abrir `Iniciar.cmd`. `Conversor.py` conserva el acceso anterior.

Introduce una cantidad, selecciona **De** y **A** y pulsa **Convertir**. Admite coma o punto decimal. **⇄** intercambia las unidades sin modificar la cantidad ni convertir automáticamente; deja el resultado en **—**. **Limpiar** borra el contenido y restablece mm → m. Intro convierte, Escape limpia y Alt+I intercambia.

## Informar de un error

Abre [una incidencia](https://github.com/matiasdurann/conversor-longitud/issues/new/choose) y explica los pasos, el resultado esperado y lo que ocurrió. No publiques datos personales ni credenciales.

Las propuestas de corrección deben pasar las pruebas y presentarse como pull request para la revisión final de **matiasdurann**. No se integran automáticamente.

## Pruebas

Solo lógica, sin ventana ni CustomTkinter:

```console
python -m unittest -v tests.test_logica
```

Todas las pruebas, con dependencias y sesión gráfica:

```console
python -m unittest discover -s tests -v
python -m unittest -v test_conversor.py
```

GitHub Actions ejecuta estas comprobaciones en Windows en cada push y pull request. No evalúa ni corrige por sí solo incidencias escritas por usuarios.

Consulta [SPEC.md](SPEC.md), [LEEME.md](LEEME.md) y [MEJORAS/INSTRUCCIONES.md](MEJORAS/INSTRUCCIONES.md). El audio y el PDF originales se conservan solo en el ordenador del propietario y no forman parte de este repositorio público.
