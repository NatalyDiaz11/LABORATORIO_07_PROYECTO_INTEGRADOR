# Priorización de historias de usuario - Khanauky

## 1. Priorización mediante MoSCoW

La técnica MoSCoW permite clasificar las historias de usuario según su importancia para el funcionamiento del sistema.

| Historia | Clasificación | Justificación |
|---|---|---|
| HU-01 Registrar cliente | MUST | Es necesario contar con información del cliente para asociarlo correctamente a los pedidos. |
| HU-02 Registrar pedido | MUST | Es una funcionalidad principal del sistema porque inicia el proceso de atención al cliente. |
| HU-03 Consultar y actualizar stock | MUST | Es indispensable para verificar la disponibilidad de productos y evitar inconsistencias. |
| HU-04 Registrar producción | SHOULD | Es importante para mantener actualizada la disponibilidad de productos, aunque puede trabajarse después de las funciones principales de pedidos y stock. |
| HU-05 Consultar estado del pedido | SHOULD | Aporta seguimiento y mejora la atención al cliente, pero el sistema puede registrar pedidos aunque esta función todavía no esté completa. |

---

## 2. Priorización mediante técnica de 100 puntos

Se distribuyen 100 puntos entre las historias de usuario de acuerdo con su importancia para el proyecto.

| Historia | Puntos asignados |
|---|---:|
| HU-01 Registrar cliente | 15 |
| HU-02 Registrar pedido | 30 |
| HU-03 Consultar y actualizar stock | 25 |
| HU-04 Registrar producción | 15 |
| HU-05 Consultar estado del pedido | 15 |
| **Total** | **100** |

---

## 3. Orden de prioridad

De acuerdo con las dos técnicas utilizadas, el orden de prioridad propuesto es:

1. HU-02 Registrar pedido.
2. HU-03 Consultar y actualizar stock.
3. HU-01 Registrar cliente.
4. HU-04 Registrar producción.
5. HU-05 Consultar estado del pedido.

---

## 4. Análisis

Las técnicas utilizadas coinciden en que las funcionalidades relacionadas con el registro de pedidos y el control de stock tienen mayor prioridad.

HU-02 es prioritaria porque representa el inicio del proceso principal de atención al cliente.

HU-03 también tiene alta prioridad porque permite conocer la disponibilidad real de los productos y reduce el riesgo de registrar o atender pedidos sin existencias suficientes.

HU-01 es necesaria para relacionar correctamente los pedidos con sus clientes.

HU-04 y HU-05 siguen siendo importantes, pero pueden desarrollarse después de asegurar las funciones centrales de registro de pedidos y control de stock.

---

## Resultado

La utilización de MoSCoW y la técnica de 100 puntos permite justificar el orden de desarrollo de las historias de usuario y facilita la selección de funcionalidades para los primeros Sprint del proyecto Khanauky.
