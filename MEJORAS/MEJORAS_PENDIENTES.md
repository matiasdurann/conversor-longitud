# Mejoras pendientes

1.3.0: propuesta visual oscura de la incidencia #1 preparada en rama separada; pendiente de revisión final e integración por el propietario mediante PR.

- Conectar una integración de IA para preparar correcciones a partir de incidencias; requiere configuración y permisos del propietario. La CI de pruebas no corrige errores automáticamente.
- Configurar protección de main en GitHub si se quiere exigir técnicamente una PR y comprobaciones antes de integrar; CODEOWNERS por sí solo no lo exige.

1.2.1: especificado y cubierto por prueba el intercambio sin conversión automática, con texto intacto y resultado `—`. No se añaden funciones pendientes para esta mejora.

## Estado 1.2.0

- CustomTkinter instalado con autorización; ventana y pruebas gráficas verificadas. No quedan bloqueos de la implementación especificada. Las pruebas de lógica no requieren esta dependencia.

Ideas opcionales para valorar antes de implementarlas:

- Copiar el resultado con un botón.
- Historial de conversiones de la sesión.
- Formato científico o área desplazable para cantidades de cientos de cifras que no caben en el panel.

Pendiente de la entrega original: contrastar el audio con la transcripción del PDF cuando se disponga de una herramienta de audio. No se han supuesto peticiones adicionales de la grabación.
