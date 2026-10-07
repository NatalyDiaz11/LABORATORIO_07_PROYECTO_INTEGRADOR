# CU - Atender pedido

## Objetivo

Representar el flujo principal de atención de un pedido en Khanauky, considerando la identificación del cliente, revisión del pedido, disponibilidad de productos, coordinación con almacén y producción, actualización del stock y confirmación final del pedido.

## Flujo principal

1. El vendedor recibe o selecciona un pedido pendiente.
2. El sistema muestra la información del cliente y el detalle del pedido.
3. El vendedor revisa los productos y cantidades solicitadas.
4. El sistema verifica si el cliente se encuentra registrado.
5. El sistema consulta la disponibilidad de los productos en stock.
6. Si todos los productos están disponibles, el pedido continúa.
7. Si algún producto requiere producción, se registra la necesidad de producción.
8. Producción actualiza el estado del producto cuando se encuentra disponible.
9. Almacén verifica y actualiza las existencias correspondientes.
10. El vendedor revisa nuevamente el pedido y confirma la atención.
11. El sistema actualiza el stock según los productos asignados al pedido.
12. El sistema actualiza el estado del pedido a atendido o confirmado.
13. El sistema muestra la confirmación de la operación.
14. Fin.

## Excepciones

### E1 - Cliente no registrado

Si el cliente no se encuentra registrado, el vendedor debe registrar o actualizar la información necesaria del cliente antes de continuar con la atención del pedido.

Una vez completado el registro, el flujo regresa a la revisión del pedido.

### E2 - Stock insuficiente

Si uno o más productos no cuentan con stock suficiente, el sistema informa la situación.

El vendedor puede:

- modificar la cantidad solicitada;
- retirar el producto del pedido;
- consultar si el producto puede ser producido;
- dejar el pedido pendiente.

El pedido no debe confirmarse mientras la disponibilidad no haya sido resuelta.

### E3 - Producto requiere producción

Si un producto no se encuentra disponible en almacén pero puede ser producido, el pedido queda en estado pendiente de producción.

Producción registra o actualiza el estado correspondiente.

Cuando el producto está listo, almacén actualiza las existencias y el flujo continúa con la confirmación del pedido.

### E4 - Error al actualizar stock

Si ocurre un error al actualizar las existencias después de confirmar el pedido, el sistema debe evitar que el pedido quede registrado con información inconsistente.

La operación debe marcarse como pendiente de revisión hasta corregir el problema.

## Compensación

### C1 - Restaurar información anterior

Si la atención del pedido falla después de modificar el stock o el estado del pedido, el sistema debe restaurar los valores anteriores o mantener la operación como pendiente.

Esto evita que exista un pedido confirmado con cantidades incorrectas en almacén.

## Reglas del proceso

- Un pedido no puede confirmarse si no existe disponibilidad suficiente.
- Producción y almacén se representan como funciones diferentes aunque una misma persona pueda cumplir ambas responsabilidades.
- El stock solo debe actualizarse cuando la atención del pedido haya sido confirmada.
- El pedido debe mantener un estado identificable durante todo el proceso.
- Los cambios realizados deben conservar coherencia entre pedido, producción y almacén.

## Diagrama Mermaid

```mermaid
flowchart TD

A([Inicio]) --> B[Recibir o seleccionar pedido pendiente]

B --> C[Mostrar cliente y detalle del pedido]

C --> D{¿Cliente registrado?}

D -- No --> E[Registrar o actualizar cliente]
E --> C

D -- Sí --> F[Revisar productos y cantidades]

F --> G[Consultar disponibilidad en stock]

G --> H{¿Stock suficiente?}

H -- Sí --> I[Preparar atención del pedido]

H -- No --> J{¿Producto puede producirse?}

J -- No --> K[Modificar pedido o dejar pendiente]

K --> L{¿Continuar con pedido?}

L -- Sí --> F
L -- No --> Z([Fin: pedido pendiente o cancelado])

J -- Sí --> M[Registrar necesidad de producción]

M --> N[Producción actualiza estado del producto]

N --> O{¿Producto disponible?}

O -- No --> M

O -- Sí --> P[Almacén actualiza existencias]

P --> I

I --> Q[Confirmar atención del pedido]

Q --> R[Actualizar stock]

R --> S{¿Actualización correcta?}

S -- No --> T[Restaurar información anterior]

T --> U[Marcar pedido pendiente de revisión]

U --> Z

S -- Sí --> V[Actualizar estado del pedido]

V --> W[Mostrar confirmación]

W --> X([Fin: pedido atendido])

