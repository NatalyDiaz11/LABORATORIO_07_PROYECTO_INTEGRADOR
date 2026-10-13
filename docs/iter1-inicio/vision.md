# Documento de Visión v1 - Khanauky

## 1. Propósito
Desarrollar una propuesta de sistema que permita organizar y controlar de manera más eficiente los procesos principales de Khanauky, especialmente la atención de pedidos, el manejo de clientes, el control del inventario, la producción y el almacén.

## 2. Problema
Actualmente varios procesos del negocio se realizan de forma manual o dependen de la coordinación directa entre los trabajadores. Esto puede generar pérdida de información, dificultades para conocer el estado de un pedido, errores en el control del inventario y retrasos en la atención al cliente.

## 3. Alcance

### Incluye
- Gestión de clientes.
- Atención de pedidos.
- Consulta y actualización del stock.
- Registro de información relacionada con producción.
- Control de almacén.
- Seguimiento del estado de los pedidos.
- Consulta de información necesaria para atender al cliente.

### No incluye
- Pagos en línea.
- Integración con bancos.
- Aplicación móvil.
- Gestión contable completa.
- Gestión de recursos humanos.
- Seguimiento GPS de repartos.

En esta iteración, el cliente realiza la solicitud del pedido, pero no registra directamente la información en el sistema. El vendedor es responsable de registrar y gestionar el pedido a partir de la solicitud del cliente.

## 4. Interesados

| Rol | Necesidad |
|---|---|
| Cliente | Realizar pedidos y recibir una atención adecuada. |
| Vendedor | Registrar y gestionar la información necesaria para atender los pedidos. |
| Producción | Conocer los pedidos que requieren elaboración y actualizar su estado. |
| Almacén | Consultar y actualizar las existencias de productos e insumos. |
| Administrador | Consultar y controlar la información general del sistema. |

## 5. Objetivos medibles

- Validar la disponibilidad antes de confirmar el 100 % de los pedidos.
- Mantener un estado identificable para el 100 % de los pedidos registrados.
- Evitar que un pedido sea confirmado cuando falle la actualización del stock.
- Mantener trazabilidad entre pedido, producción, almacén y stock en las operaciones atendidas.
- Reducir inconsistencias entre la información del pedido y las existencias registradas mediante validaciones antes de la confirmación.

## 6. Requisitos de alto nivel
- REQ-001: Registrar y actualizar información del cliente.
- REQ-002: Atender pedido.
- REQ-003: Consultar y actualizar stock.
La actualización del stock asociada a la atención de un pedido se realiza al completar correctamente la operación. Almacén también puede realizar actualizaciones manuales por ingresos, reposiciones o ajustes que no estén directamente asociados a un pedido.
- REQ-004: Gestionar información de producción.
- REQ-005: Gestionar información de almacén.
- REQ-006: Consultar el estado de los pedidos.

## 7. Restricciones
- El sistema se desarrollará como parte del proyecto académico Khanauky.
- El alcance estará limitado a los procesos definidos por el equipo.
- Las funciones deberán mantener coherencia con los casos de uso y diagramas desarrollados.
- Una misma persona puede cumplir varias responsabilidades dentro de la empresa, pero las funciones deben mantenerse representadas de forma independiente cuando correspondan a procesos diferentes.
