# Casos de uso - Khanauky

## CU-001: Gestionar clientes
Cubre: REQ-001

- Actor principal: Vendedor
- Descripción: Permite registrar y consultar información de clientes.

## CU-002: Atender pedido
Cubre: REQ-002, REQ-003, REQ-004, REQ-005 y REQ-006

- Actor principal: Vendedor
- Actores relacionados: Cliente, Producción y Almacén

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
- Stock insuficiente.
- Error durante la actualización del stock.
- Pedido pendiente de revisión.
- Información del cliente incompleta.
