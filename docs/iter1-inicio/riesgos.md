# Riesgos del proyecto - Khanauky

| ID | Fase | Riesgo | Probabilidad | Impacto | Mitigación | Responsable |
|---|---|---|---|---|---|---|
| RSK-001 | Inicio | Alcance ambiguo o incorporación de funciones que no corresponden a esta iteración. | Media | Alto | Validar el Documento de Visión, especialmente las secciones "Incluye" y "No incluye", antes de continuar con nuevos artefactos. | Analista |
| RSK-002 | Elaboración | Inconsistencia entre el estado del pedido, stock, producción y almacén. | Media | Alto | Definir reglas claras de actualización y mantener trazabilidad entre pedido, stock, producción y almacén. | Arquitecto / Analista |
| RSK-003 | Elaboración | Modelar Producción y Almacén como una sola función y perder responsabilidades relevantes del proceso. | Media | Alto | Mantener ambas funciones diferenciadas en casos de uso, actividades y demás modelos, aunque una misma persona pueda ejecutarlas. | Analista |
| RSK-004 | Construcción | Confirmar un pedido con stock insuficiente o con información desactualizada. | Media | Alto | Validar disponibilidad antes de confirmar el pedido y probar escenarios con cantidades superiores al stock disponible. | Desarrollador |
| RSK-005 | Construcción | Fallo durante la actualización de stock después de confirmar un pedido. | Media | Alto | Implementar compensación C1 para restaurar la información anterior o dejar el pedido pendiente de revisión. | Desarrollador |
| RSK-006 | Transición | El usuario no comprende correctamente los estados del pedido o el flujo de atención. | Media | Medio | Ejecutar pruebas de aceptación, registrar observaciones y preparar un manual breve de uso. | Líder del proyecto |

## Tarjetas sugeridas para la lista "Riesgos" en Trello

### RSK-001 - Alcance ambiguo
- Revisar Documento de Visión.
- Confirmar secciones "Incluye" y "No incluye".
- Validar alcance con el equipo.

### RSK-002 - Inconsistencia entre pedido, stock, producción y almacén
- Revisar el flujo de Atender pedido.
- Verificar cambios de estado.
- Comprobar actualización de stock.
- Validar participación de Producción y Almacén.

### RSK-003 - Pérdida de funciones por acumulación de roles
- Revisar casos de uso y actividades.
- Mantener funciones separadas.
- Confirmar responsabilidades del negocio.

### RSK-004 - Pedido confirmado sin stock suficiente
- Validar disponibilidad antes de confirmar.
- Probar cantidades mayores al stock disponible.
- Comprobar mensaje de stock insuficiente.

### RSK-005 - Error en actualización de stock
- Verificar compensación C1.
- Restaurar información anterior ante error.
- Mantener pedido pendiente de revisión.

### RSK-006 - Dificultad de uso
- Realizar prueba con usuario.
- Registrar observaciones.
- Elaborar manual breve.
