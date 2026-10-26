# Casos de uso - Khanauky

## CU-001: Gestionar clientes
Cubre: REQ-001

- Actor principal: Vendedor
- Descripción: Permite registrar y consultar información de clientes.

---

## CU-002: Atender pedido
Cubre: REQ-003, REQ-004, REQ-005 y REQ-006

- Actor principal: Vendedor
- Actores relacionados: Cliente, Producción y Almacén

### Flujo principal
1. El vendedor recibe o selecciona un pedido pendiente.
2. El sistema muestra la información del cliente y el detalle del pedido.
3. El vendedor revisa los productos y cantidades solicitadas.
4. El sistema verifica la disponibilidad de stock.
5. Si es necesario, se coordina la producción del producto.
6. Almacén confirma la salida de los productos correspondientes al pedido.
7. El sistema descuenta las cantidades entregadas y actualiza el stock registrado.
8. Para cada producto del pedido, el sistema compara la cantidad disponible con el stock mínimo definido.
9. Si la cantidad disponible queda por debajo del stock mínimo, el sistema genera una alerta informativa para Almacén.
10. La alerta de stock mínimo no impide continuar con la atención del pedido.
11. Si la actualización es correcta, se confirma la atención del pedido.
12. El estado del pedido cambia a Atendido.
13. El sistema muestra la confirmación final.

### Flujo alternativo
- Si un producto no tiene un stock mínimo configurado, el sistema informa esta condición y permite continuar con la atención del pedido sin generar la alerta de stock mínimo.

### Excepciones
- Stock insuficiente para atender el pedido.
- Error durante la actualización del stock.
- Pedido pendiente de revisión.
- Información del cliente incompleta.

---

## CU-003: Registrar pedido
Cubre: REQ-002

- Actor principal: Vendedor
- Actor relacionado: Cliente

### Flujo principal
1. El vendedor identifica o selecciona al cliente.
2. Registra los productos y cantidades solicitadas.
3. El sistema valida que los datos obligatorios estén completos.
4. El sistema registra el pedido.
5. El pedido queda con estado Pendiente.
6. El sistema muestra la confirmación del registro.

### Excepciones
- El cliente no se encuentra registrado.
- Faltan datos obligatorios del pedido.
- No se han registrado productos o cantidades.
- Ocurre un error durante el registro del pedido.
