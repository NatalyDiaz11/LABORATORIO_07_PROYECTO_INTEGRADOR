# Alcance del módulo y actores - Khanauky

## 1. Alcance del módulo

Para este laboratorio se trabajará principalmente con el módulo de gestión de pedidos del sistema Khanauky.

El módulo incluye el registro y atención de pedidos, la consulta de disponibilidad de stock, la coordinación con Producción y Almacén y la consulta del estado del pedido.

Quedan fuera de este alcance otras funciones administrativas que no participan directamente en el proceso de atención del pedido.

---

## 2. Actores y objetivos

| Actor | Tipo | Objetivos |
|---|---|---|
| Vendedor | Primario | Registrar clientes, registrar pedidos, atender pedidos y consultar el estado de los pedidos. |
| Cliente | Primario | Solicitar productos y recibir información sobre el estado de su pedido. |
| Personal de Producción | Primario | Consultar los pedidos que requieren producción y registrar información del proceso productivo. |
| Personal de Almacén | Primario | Consultar existencias, registrar salidas de productos y mantener actualizado el stock. |
| Administrador | Secundario | Supervisar la información general de pedidos, clientes, producción, almacén y stock. |

---

## 3. Casos de uso identificados

A partir de los requisitos del proyecto se identifican los siguientes casos de uso principales:

- CU-001: Gestionar clientes.
- CU-002: Atender pedido.
- CU-003: Registrar pedido.
- CU-004: Consultar y actualizar stock.
- CU-005: Registrar producción.
- CU-006: Registrar salida de almacén.
- CU-007: Consultar estado del pedido.

---

## 4. Relación general entre actores y casos de uso

El Vendedor participa principalmente en el registro de clientes, registro de pedidos, atención de pedidos y consulta de su estado.

El Personal de Producción participa cuando un pedido requiere fabricación o preparación adicional.

El Personal de Almacén interviene en la verificación de existencias y en el registro de salidas de productos.

El Cliente participa como origen de la solicitud y como receptor del pedido.

El Administrador supervisa la información general del sistema.
