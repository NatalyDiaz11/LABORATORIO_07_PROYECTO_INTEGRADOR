# Casos de uso - Khanauky

## CU-001: Gestionar clientes
Cubre: REQ-001

- Actor principal: Vendedor
- Descripción: Permite registrar y consultar información de clientes.

## CU-002: Atender pedido
Cubre: REQ-002, REQ-003, REQ-004, REQ-005 y REQ-006

- Actor principal: Vendedor
- Actores relacionados: Cliente, Producción y Almacén

### Flujo principal
1. El vendedor recibe o selecciona un pedido pendiente.
2. El sistema muestra la información del cliente y el detalle del pedido.
3. El vendedor revisa los productos y cantidades solicitadas.
4. El sistema verifica la disponibilidad de stock.
5. Si es necesario, se coordina la producción del producto.
6. Almacén actualiza las existencias.
7. El sistema actualiza el stock.
8. Si la actualización es correcta, se confirma la atención del pedido.
9. El estado del pedido cambia a Atendido.
10. El sistema muestra la confirmación final.

### Excepciones
- Stock insuficiente.
- Error durante la actualización del stock.
- Pedido pendiente de revisión.
- Información del cliente incompleta.
