# Pruebas - Khanauky

| ID | Requisito | Qué se prueba | Resultado esperado |
|---|---|---|---|
| PRU-001 | REQ-001 | Registrar y consultar un cliente con datos válidos | Cliente registrado y visible en el sistema |
| PRU-002 | REQ-002 | Registrar un pedido con productos y cantidades válidas | Pedido registrado correctamente |
| PRU-003 | REQ-003 | Consultar y actualizar el stock de un producto | Stock actualizado correctamente |
| PRU-003a | REQ-003 (CR-001) | Atender un pedido y dejar el stock por encima o igual al mínimo definido | Stock actualizado sin generar alerta |
| PRU-003b | REQ-003 (CR-001) | Atender un pedido y dejar el stock por debajo del mínimo definido | Stock actualizado y alerta generada para Almacén |
| PRU-003c | REQ-003 (CR-001) | Atender un pedido con un producto que no tiene stock mínimo configurado | El sistema informa que no existe un stock mínimo configurado, permite continuar con la atención del pedido y no genera la alerta |
| PRU-004 | REQ-004 | Registrar y consultar información de producción asociada a un pedido | Información de producción registrada y disponible |
| PRU-005 | REQ-005 | Consultar existencias y registrar una salida de almacén asociada a un pedido | Existencias actualizadas y salida registrada |
| PRU-006 | REQ-006 | Consultar el estado de un pedido | Estado del pedido mostrado correctamente |
