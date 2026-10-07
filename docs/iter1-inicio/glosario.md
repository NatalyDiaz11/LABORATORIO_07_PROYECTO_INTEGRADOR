# Glosario - Khanauky

| Término oficial | Significado | Evitar usar como sinónimo |
|---|---|---|
| Cliente | Persona que realiza o solicita un pedido. | Usuario, comprador, cuando genere ambigüedad. |
| Vendedor | Personal encargado de atender al cliente y gestionar el pedido. | Cliente, administrador. |
| Pedido | Solicitud realizada por un cliente que contiene productos y cantidades. | Venta. |
| Venta | Operación comercial confirmada a partir de un pedido atendido. | Pedido. |
| Producto | Artículo ofrecido por Khanauky. | Ítem, cuando genere ambigüedad. |
| Stock | Cantidad disponible de un producto o insumo. | Cantidad del pedido. |
| Almacén | Función encargada de controlar existencias y disponibilidad. | Stock. |
| Producción | Función encargada de elaborar o preparar productos cuando sea necesario. | Almacén. |
| Disponibilidad | Condición que indica si un producto puede ser atendido con stock o producción. | Stock suficiente, cuando no represente toda la situación. |
| Estado del pedido | Situación actual del pedido durante su atención. | Estado de venta. |
| Pedido pendiente | Pedido que todavía no puede ser confirmado o completado. | Pedido cancelado. |
| Pedido atendido | Pedido cuya atención fue completada correctamente. | Venta automática. |
| Administrador | Responsable de consultar y supervisar información general del sistema. | Vendedor. |

## Reglas de consistencia

- **Pedido y venta no son el mismo concepto.**
- El pedido existe antes de que la operación comercial quede confirmada.
- Producción y almacén son funciones diferentes, aunque una misma persona pueda asumir ambas responsabilidades.
- El término **stock** se utiliza únicamente para representar existencias disponibles.
- El estado del pedido debe mantenerse con el mismo nombre en todos los documentos y diagramas.
- El actor **Vendedor** debe conservar el mismo nombre en Visión, casos de uso, diagramas y demás artefactos.
