# Registro de cambios

## Publicación y mantenimiento en GitHub — 2026-10-20

- Publicación autorizada de código, pruebas y documentación; se excluyen audio, PDF, cachés y configuración local mediante .gitignore.
- README de instalación, formulario de errores, plantilla de PR y CODEOWNERS para la revisión final del propietario.
- GitHub Actions ejecuta unittest en Windows para pushes y pull requests. Sin integración de IA con credenciales ni fusión automática.
- No cambia el programa: se conserva la versión 1.2.1.

## 1.2.1 — 2026-10-20

- Ajustado el intercambio existente: el resultado pasa a `—`, sin conversión automática, conservando literalmente la cantidad. Se mantiene Convertir y la reversibilidad del intercambio.
- Añadida aceptación con unittest en tests/test_mejora.py para las nueve combinaciones, texto exacto, doble intercambio y conversión posterior.
- SPEC.md actualizado; sin dependencias nuevas ni cambios en el sistema de automatización.
- Verificación: siete pruebas en tests y las cinco anteriores superadas; revisión visual del intercambio m → mm con resultado `—` completada.

## 1.2.0 — 2026-10-20

- Implementación del plan confirmado en SPEC.md: migración de la interfaz a CustomTkinter en app.py y extracción de la lógica Decimal existente a logica.py.
- requirements.txt declara CustomTkinter 5.2.2. Su instalación requiere autorización expresa y no se ejecuta automáticamente al abrir el programa.
- Se conservan unidades, decimales, signos, validación de escritura y pegado, intercambio, limpieza y atajos.
- Conversor.py mantiene el acceso anterior y las importaciones de lógica; Iniciar.cmd abre app.py. Los archivos originales se conservan.
- Nuevas pruebas independientes con unittest en tests/test_logica.py; las pruebas anteriores apuntan a la interfaz actual.
- Instalación de CustomTkinter 5.2.2 y sus dependencias autorizada expresamente por el usuario y completada.
- Verificación: seis pruebas de lógica y cinco de regresión superadas, incluidas escritura, pegado, limpieza, intercambio, atajos y pulsaciones repetidas. Ventana CustomTkinter final abierta y revisada visualmente. No hay llamadas de red en la aplicación.
- Corregida la limpieza de callbacks pendientes de CustomTkinter al cerrar ventanas de prueba para evitar avisos Tcl entre pruebas.

## 1.1.0 — 2026-10-20

- Mejora sobre el programa original en Python/Tkinter; se conserva el cálculo exacto con Decimal y todas las unidades.
- Validación de escritura y pegado: rechaza letras, espacios, separadores duplicados y otros caracteres incorrectos, con aviso claro. Se conservan los signos iniciales para números negativos.
- La conversión sigue rechazando cantidades vacías y estados de edición incompletos.
- Campo numérico más grande, selectores De/A, intercambio de unidades con botón y Alt+I, y resultado más visible.
- Limpiar ahora restablece mm como origen y m como destino, además de borrar cantidad, resultado y avisos.
- Pruebas ampliadas para escritura, portapapeles, intercambio, limpieza, teclado y pulsaciones repetidas.
- Verificación: cinco pruebas automatizadas superadas, incluidas las nueve combinaciones y controles Tkinter reales. Revisión visual de la ventana final; se amplió su altura y se ajustó el texto inicial para corregir un recorte del panel de resultado. Funcionamiento local sin dependencias ni llamadas de red.
- Se añade esta carpeta de mantenimiento; no se modifican los archivos originales de audio y PDF ni se añaden dependencias o conexiones de red.

## 1.0.0 — 2026-10-20

- Versión inicial: nueve conversiones, decimales, validación al calcular, interfaz local y botones Convertir/Limpiar.
