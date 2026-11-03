# Registro de refactor - Khanauky

## 1. Propósito

El objetivo del refactor es mejorar la organización del modelo conceptual del sistema Khanauky, asegurando que cada clase mantenga responsabilidades coherentes y evitando dependencias innecesarias entre clases.

---

## 2. Problema identificado

Durante la revisión del modelo se identificó que parte de la lógica relacionada con el cálculo de subtotales de productos podía quedar ubicada directamente dentro de la clase Pedido.

Sin embargo, Pedido representa principalmente la información general de la operación, como fecha, estado y total.

El cálculo asociado a cada producto y cantidad corresponde mejor a la clase DetallePedido.

---

## 3. Situación inicial

Inicialmente se podía considerar que Pedido realizara operaciones como:

- registrar()
- atender()
- consultarEstado()
- actualizarEstado()
- calcularSubtotal()

Esto generaba una responsabilidad adicional dentro de Pedido, ya que calcular el subtotal depende de la cantidad y del precio unitario de cada producto.

---

## 4. Refactor aplicado

Se decidió retirar la operación:

`calcularSubtotal()`

de la clase Pedido.

La operación fue asignada a:

`DetallePedido`

De esta manera:

### Pedido
Mantiene responsabilidades relacionadas con:

- registro del pedido;
- atención del pedido;
- estado;
- total general.

### DetallePedido
Mantiene responsabilidades relacionadas con:

- producto asociado;
- cantidad solicitada;
- precio unitario;
- subtotal.

---

## 5. Justificación

Este cambio mejora la cohesión porque cada clase mantiene responsabilidades más específicas.

Pedido se concentra en gestionar la información general del pedido.

DetallePedido se encarga de la información específica de cada producto dentro del pedido.

También se reduce el acoplamiento, ya que Pedido no necesita conocer directamente los datos necesarios para calcular el subtotal de cada producto.

---

## 6. Resultado del refactor

Después del refactor, el modelo queda organizado de la siguiente manera:

### Pedido

**Operaciones**
- registrar()
- atender()
- consultarEstado()
- actualizarEstado()

### DetallePedido

**Operaciones**
- calcularSubtotal()
- registrarDetalle()

---

## 7. Conclusión

El refactor aplicado permite mantener una mejor distribución de responsabilidades dentro del modelo conceptual de Khanauky.

La separación entre Pedido y DetallePedido mejora la cohesión de las clases y facilita futuras modificaciones del sistema.
