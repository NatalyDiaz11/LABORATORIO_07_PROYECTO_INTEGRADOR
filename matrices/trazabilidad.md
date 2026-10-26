# Matriz de trazabilidad - Khanauky

| Req | Descripción | CU | Clase | Prueba | Último CR | ¿Cubierto? |
|---|---|---|---|---|---|---|
| REQ-001 | Registrar y consultar información de clientes | CU-001 | CLS-Cliente | PRU-001 | - | Sí |
| REQ-002 | Registrar y gestionar pedidos | CU-003 | CLS-Pedido | PRU-002 | - | Sí |
| REQ-003 | Consultar y actualizar el stock de productos y gestionar la alerta de stock mínimo | CU-002 | CLS-Stock | PRU-003, PRU-003a, PRU-003b, PRU-003c | CR-001 | Sí |
| REQ-004 | Registrar y consultar información de producción asociada a los pedidos | CU-002 | CLS-Produccion | PRU-004 | - | Sí |
| REQ-005 | Consultar existencias y registrar salidas de almacén asociadas a los pedidos | CU-002 | CLS-Almacen | PRU-005 | - | Sí |
| REQ-006 | Consultar el estado de los pedidos | CU-002 | CLS-Pedido | PRU-006 | - | Sí |

## Cobertura de trazabilidad

Requisitos totales: 6

Requisitos con una prueba asociada: 6

Cobertura de trazabilidad: 100 %

Estado de ejecución de pruebas: Pendiente.

El 100 % indica que todos los requisitos tienen al menos una prueba definida. No significa que todas las pruebas hayan sido ejecutadas y validadas correctamente.

## Cambio aplicado

CR-001 modificó REQ-003 para incorporar una alerta de stock mínimo durante la atención de pedidos.
