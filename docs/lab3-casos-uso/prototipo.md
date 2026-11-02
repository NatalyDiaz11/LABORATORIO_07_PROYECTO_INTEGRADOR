# Prototipo y flujo de navegación - Khanauky

## 1. Propósito

En esta sección se presentan interfaces reales del sistema Khanauky relacionadas con los casos de uso definidos en el Laboratorio 3.

Cada pantalla utiliza un identificador de trazabilidad para relacionarla con el caso de uso correspondiente.

---

## 2. Interfaces del sistema

### UI-CU001-01 - Clientes registrados

Esta pantalla permite consultar los clientes registrados en Khanauky y visualizar información como tipo de cliente, DNI/RUC, teléfono, distrito y bidones pendientes.

**Caso de uso relacionado:** CU-001 Gestionar clientes.

![UI-CU001-01 - Clientes registrados](../../evidencias/laboratorio3/UI-CU001-01-clientes-registrados.png)

---

### UI-CU003-01 - Registrar venta o pedido

Esta interfaz permite registrar una venta presencial seleccionando productos, cantidades, método de pago, tipo de comprobante, descuento y monto pagado.

Esta pantalla representa parte del proceso utilizado para registrar una solicitud de productos en el sistema.

**Caso de uso relacionado:** CU-003 Registrar pedido.

![UI-CU003-01 - Registrar pedido](../../evidencias/laboratorio3/UI-CU003-01-registrador-venta-pedido.png)

---

### UI-CU005-01 - Registro de producción

Esta pantalla permite registrar nuevos lotes de producción indicando producto, fecha de producción, unidades producidas, unidades defectuosas y fecha de vencimiento.

También permite consultar los lotes registrados y las unidades disponibles.

**Caso de uso relacionado:** CU-005 Registrar producción.

![UI-CU005-01 - Producción](../../evidencias/laboratorio3/UI-CU005-01-produccion-lotes.png)

---

### UI-CU007-01 - Estado de ventas y pedidos

Esta interfaz muestra las órdenes registradas y permite consultar información como fecha, cliente, total, saldo, tipo de entrega y estado.

El estado puede reflejar diferentes etapas del proceso, como Venta Registrada, Pago Confirmado, Entregado o Cancelado.

**Caso de uso relacionado:** CU-007 Consultar estado del pedido.

![UI-CU007-01 - Estado de pedidos](../../evidencias/laboratorio3/UI-CU007-01-estado-reporte-ventas.png)

---

### UI-CU007-02 - Seguimiento de pedidos

Esta pantalla permite visualizar el avance de un pedido mediante diferentes estados.

Por ejemplo:

Venta Registrada → Pago Confirmado → Entregado.

Esto permite al usuario conocer en qué etapa se encuentra actualmente su pedido.

**Caso de uso relacionado:** CU-007 Consultar estado del pedido.

![UI-CU007-02 - Seguimiento de pedidos](../../evidencias/laboratorio3/UI-CU007-02-seguimiento-pedidos.png)

---

## 3. Flujo de navegación

Un flujo principal del sistema puede representarse de la siguiente manera:

**Clientes → Registrar pedido/venta → Producción y disponibilidad → Seguimiento del pedido → Entrega**

El vendedor puede consultar o identificar al cliente, registrar los productos solicitados y posteriormente realizar el seguimiento de la operación.

Cuando corresponde, el proceso se relaciona con Producción y con el control de disponibilidad de productos.

Finalmente, el estado de la operación permite conocer si la venta fue registrada, si el pago fue confirmado o si el pedido fue entregado.

---

## 4. Matriz de trazabilidad interfaz - caso de uso

| ID de interfaz | Pantalla | Caso de uso |
|---|---|---|
| UI-CU001-01 | Clientes registrados | CU-001 Gestionar clientes |
| UI-CU003-01 | Registrar venta/pedido | CU-003 Registrar pedido |
| UI-CU005-01 | Lotes de producción | CU-005 Registrar producción |
| UI-CU007-01 | Reporte y estado de ventas | CU-007 Consultar estado del pedido |
| UI-CU007-02 | Seguimiento de pedidos | CU-007 Consultar estado del pedido |

---

## 5. Resultado

Las interfaces implementadas permiten comprobar que los casos de uso definidos en el modelado tienen representación dentro del sistema Khanauky.

La utilización de identificadores UI-CU permite mantener la relación entre la documentación de casos de uso y las pantallas reales de la aplicación.
