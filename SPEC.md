# Especificación del conversor

Fecha: 2026-10-20.
Estado: plan confirmado e implementado. El usuario autorizó expresamente la instalación de dependencias, realizada el 2026-10-20. Superadas seis pruebas de lógica y cinco de regresión gráfica; ventana final revisada visualmente.

## Resumen del programa actual

Aplicación de escritorio local en Python/Tkinter, versión 1.1.0, implementada en `Conversor.py`. Convierte entre milímetros, centímetros y metros en las nueve combinaciones. Usa Decimal para conservar la precisión; admite enteros, decimales con coma o punto y signos iniciales. Rechaza letras y pegados incorrectos. Ofrece selectores De/A, intercambio, Convertir, Limpiar y resultado con unidad. Limpiar restablece mm → m. Incluye navegación con Tab, Intro para convertir, Escape para limpiar y Alt+I para intercambiar. No necesita Internet para funcionar.

## Alcance acordado para la próxima implementación

- Mantener las funciones existentes descritas, con una interfaz sencilla y adaptable en Python y CustomTkinter.
- Reutilizar la lógica existente, separándola de la interfaz; funciones sencillas y sin funciones adicionales.
- `app.py`: ventana CustomTkinter, validación de entrada y pegado, selectores y acciones.
- `logica.py`: unidades, validación numérica, conversión exacta y formato; sin dependencia de la interfaz.
- `requirements.txt`: dependencia CustomTkinter y versión compatible comprobada al implementar. No instalar paquetes sin autorización explícita.
- `tests/test_logica.py`: pruebas con unittest para las nueve combinaciones, enteros, decimales, cero, negativos, precisión, formato y entradas vacías o incorrectas. Deben poder ejecutarse sin abrir ventanas ni instalar CustomTkinter.
- Mantener los originales de audio y PDF. Adaptar `Conversor.py` como lanzador compatible de `app.py`, conservando las importaciones públicas de lógica cuando sea necesario. Mantener `Iniciar.cmd` como acceso de apertura y actualizar las pruebas anteriores para que no prueben una interfaz obsoleta.
- Actualizar LEEME y la carpeta MEJORAS para reflejar la estructura, validación, historial y versión 1.2.0, sin añadir funciones al producto.
- Sin servidores, base de datos, conexiones de red en ejecución, Git push ni PR.

Actualización autorizada el 2026-10-20: publicar código, pruebas y documentación en el repositorio público matiasdurann/conversor-longitud. Se autoriza el push inicial; audio y PDF quedan excluidos. Añadir formulario de incidencias, pruebas GitHub Actions y propuestas de corrección en PR con revisión final del propietario. Esta autorización sustituye la prohibición anterior de push. La aplicación sigue funcionando localmente sin red. La ejecución de una IA al recibir incidencias necesita una integración conectada; no se considera activa por publicar estos archivos.

## Plan de cuatro pasos

1. Confirmar esta especificación y comprobar si CustomTkinter ya está instalado. Si falta, solicitar autorización específica antes de instalar dependencias; mientras tanto puede verificarse la lógica independiente.
2. Extraer la lógica existente a `logica.py` y crear `tests/test_logica.py` con unittest, conservando el cálculo Decimal y las reglas actuales de entrada.
3. Adaptar la interfaz a CustomTkinter en `app.py`, preparar `requirements.txt` y mantener compatibles los accesos existentes. Conservar Convertir, Limpiar, intercambio y teclado.
4. Ejecutar las pruebas, corregir fallos y revisar la ventana si la dependencia está disponible. Actualizar MEJORAS y las instrucciones para abrirla con `python app.py`, indicando expresamente cualquier comprobación bloqueada.

## Decisiones y limitaciones

- La petición actual autoriza cambiar Tkinter por CustomTkinter; sustituye la preferencia anterior de mantener la biblioteca gráfica. Python se conserva.
- La conservación de archivos y funciones se resuelve con la adaptación del acceso anterior, sin mantener dos aplicaciones independientes.
- Los signos iniciales + y - se conservan como parte de los números; no se permiten símbolos arbitrarios. Un signo o separador aislado puede existir mientras se escribe, pero no se convierte.
- Sigue pendiente contrastar el audio original con la transcripción del PDF por falta de herramienta de audio; esta limitación no impide la reorganización solicitada.
- La confirmación del plan y la autorización para instalar dependencias son decisiones separadas.

## Criterios de aceptación

### Mejora 1.2.1: intercambiar unidades (2026-10-20)

Se adapta el botón ⇄ existente (Intercambiar unidades), sin duplicarlo. Al pulsarlo intercambia Origen y Destino; conserva exactamente el texto de Cantidad/Valor, incluidos ceros, signo y separador decimal; deja el resultado en `—` y no ejecuta ninguna conversión. Dos pulsaciones restauran las unidades iniciales. Convertir mantiene su comportamiento. El indicador inicial y Limpiar mantienen su texto anterior.

Aceptación: mm → m pasa a m → mm; texto intacto; resultado `—`; doble intercambio reversible; regresión anterior sin fallos. `tests/test_mejora.py` comprueba el botón real y que no se llama a convertir durante el intercambio. Sin instalar dependencias ni cambiar unittest o el sistema de automatización.

Las pruebas de lógica sin ventana se ejecutan ahora con `python -m unittest -v tests.test_logica`; `python -m unittest discover -s tests -v` incluye también esta prueba gráfica y requiere sesión de escritorio.

Las nueve conversiones son correctas, sin redondeos binarios; la entrada y el pegado rechazan caracteres incorrectos; cantidades vacías o incompletas no generan resultados; intercambio y limpieza cumplen el comportamiento actual; la ventana conserva un diseño sencillo, resultado visible y teclado. Las pruebas de lógica pasan con `python -m unittest discover -s tests -v`. La aplicación abre con `python app.py` cuando CustomTkinter está disponible. Se documenta el resultado real de las verificaciones y se conserva el contenido original del proyecto.
