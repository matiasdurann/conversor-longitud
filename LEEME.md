# Conversor de longitud

Aplicación local de Python 3 con CustomTkinter (versión 1.2.1). Requiere la dependencia de requirements.txt; una vez instalada funciona sin conexión a Internet.

## Ejecutar

En Windows, haz doble clic en `Iniciar.cmd` o ejecuta `python app.py`. `Conversor.py` sigue funcionando como acceso compatible. Si falta CustomTkinter, la instalación propuesta es `python -m pip install -r requirements.txt`; requiere autorización explícita y no se realiza automáticamente.

Escribe una cantidad, elige las unidades y pulsa **Convertir** (o Intro). Admite decimales con coma o punto, cero y números negativos. No uses separadores de miles. **Limpiar** (o Escape) borra cantidad, resultado y avisos; restablece las unidades iniciales (mm a m). El resultado se invalida al modificar la cantidad o las unidades para evitar mostrar una equivalencia anterior.

## Archivos originales y requisitos

Se revisó íntegramente `transcripcion_audio_conversor.pdf` (una página). Solicita mm, cm y m, cantidad numérica, origen, destino, conversión, resultado y botón para limpiar; no impone tecnología. El mensaje del usuario concreta la validación, los decimales y el borrado de cantidad y resultado. Se ha elegido una aplicación de escritorio Python conforme a su preferencia.

Se localizó `Cipfp Misericòrdia.m4a`. No se pudo escuchar ni transcribir directamente: el entorno no dispone de una herramienta de transcripción de audio. Se utilizó la transcripción del PDF, sin poder contrastar su fidelidad con la grabación. Queda pendiente únicamente esa comparación para confirmar posibles peticiones del audio omitidas en el documento.

## Comprobaciones

Pruebas independientes de lógica: `python -m unittest -v tests.test_logica`. No abren ventanas ni necesitan CustomTkinter. `python -m unittest discover -s tests -v` incluye también la prueba gráfica del intercambio. La interfaz está en app.py y las conversiones en logica.py. Consulta SPEC.md para el alcance confirmado.

Verificación 1.2.0: CustomTkinter instalado con autorización, seis pruebas de lógica y cinco de regresión superadas y ventana revisada visualmente. Para abrirla ahora: `python app.py` o doble clic en `Iniciar.cmd`.

Ejecutar `python -m unittest -v test_conversor.py`. Incluye las nueve combinaciones de unidades, decimales, entradas inválidas y acciones de los botones.

## Versión 1.1.0

La entrada rechaza letras y pegados inválidos. El botón ⇄ o Alt+I intercambia las unidades. Tab recorre los controles; Intro convierte y Escape limpia. Los signos + y - se conservan para permitir los números negativos existentes. El historial y las instrucciones de mantenimiento están en `MEJORAS/`.
