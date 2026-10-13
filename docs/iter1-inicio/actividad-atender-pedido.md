# CU-002 - Atender pedido

## Objetivo

Representar el flujo principal de atención de un pedido en Khanauky, considerando la identificación del cliente, revisión del pedido, disponibilidad de productos, coordinación con almacén y producción, actualización del stock y confirmación final del pedido.

## Flujo principal

1. El vendedor recibe o selecciona un pedido pendiente.
2. El sistema muestra la información del cliente y el detalle del pedido.
3. El sistema verifica si el cliente se encuentra registrado.
4. El vendedor revisa los productos y cantidades solicitadas.
5. El sistema consulta la disponibilidad de los productos en stock.
6. Si todos los productos están disponibles, el pedido continúa.
7. Si algún producto requiere producción, se registra la necesidad de producción.
8. Producción actualiza el estado del producto cuando se encuentra disponible.
9. Almacén verifica y actualiza las existencias correspondientes.
10. El vendedor revisa nuevamente el pedido.
11. El sistema actualiza el stock correspondiente a los productos que serán atendidos.
12. Si la actualización del stock se realiza correctamente, el sistema confirma la atención del pedido.
13. El sistema actualiza el estado del pedido a Atendido.
14. El sistema muestra la confirmación de la operación.
15. Fin.

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

### C1 - Restaurar información o mantener el pedido pendiente

Si ocurre un error durante la actualización del stock, el sistema debe intentar restaurar los valores anteriores cuando sea posible hacerlo de forma segura.

Si no puede garantizarse una restauración consistente, el pedido debe mantenerse en estado Pendiente de revisión y no debe confirmarse.

Esto evita que exista un pedido confirmado con cantidades incorrectas en el stock.
## Reglas del proceso

- Un pedido no puede confirmarse si no existe disponibilidad suficiente.
- La confirmación definitiva del pedido solo debe realizarse después de que la actualización del stock termine correctamente.
- Producción es responsable de elaborar o preparar los productos que no se encuentran disponibles y de actualizar su estado de producción.
- Almacén es responsable de controlar las existencias, registrar ingresos y salidas de productos y mantener actualizado el stock disponible.
- Producción y Almacén se mantienen como funciones diferentes aunque una misma persona pueda asumir ambas responsabilidades.
- El estado del pedido debe mantenerse identificable durante todo el proceso.
- Los cambios realizados deben conservar coherencia entre pedido, producción, almacén y stock.

## Diagrama Mermaid

```mermaid
flowchart TD

A([Inicio]) --> B[Recibir o seleccionar pedido pendiente]
B --> C[Mostrar cliente y detalle del pedido]
C --> D{Cliente registrado}

D -- No --> E[Registrar o actualizar cliente]
E --> C

D -- Si --> F[Revisar productos y cantidades]
F --> G[Consultar disponibilidad en stock]
G --> H{Stock suficiente}

H -- Si --> I[Preparar atencion del pedido]

H -- No --> J{Producto puede producirse}

J -- No --> K[Modificar pedido o dejar pendiente]
K --> L{Continuar con el pedido}

L -- Si --> F
L -- No --> M([Fin: pedido pendiente o cancelado])

J -- Si --> N[Registrar necesidad de produccion]
N --> O[Produccion actualiza estado del producto]
O --> P{Producto disponible}

P -- No --> N
P -- Si --> Q[Almacen actualiza existencias]
Q --> I

I --> R[Actualizar stock]
R --> S{Actualizacion correcta}

S -- No --> T[Restaurar informacion anterior]
T --> U{Restauracion correcta}

U -- Si --> V[Dejar pedido pendiente]
U -- No --> W[Marcar pedido pendiente de revision]

V --> X([Fin: pedido pendiente])
W --> X

S -- Si --> Y[Confirmar atencion del pedido]
Y --> Z[Actualizar estado del pedido a Atendido]
Z --> AA[Mostrar confirmacion]
AA --> AB([Fin: pedido atendido])
