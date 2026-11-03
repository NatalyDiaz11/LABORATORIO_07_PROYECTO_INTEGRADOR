# Matriz requisito-clase - Khanauky

## 1. Propósito

La matriz requisito-clase permite relacionar los requisitos funcionales del sistema Khanauky con las clases que participan en su implementación.

Esta relación ayuda a comprobar que los requisitos tengan soporte dentro del modelo conceptual y permite detectar posibles brechas.

---

## 2. Matriz de trazabilidad requisito-clase

| Requisito | Descripción | Clases involucradas | Cobertura |
|---|---|---|---|
| RF-01 | Registrar y consultar información de clientes | Cliente | Sí |
| RF-02 | Registrar pedidos con productos y cantidades | Cliente, Pedido, DetallePedido, Producto | Sí |
| RF-03 | Consultar y actualizar el stock disponible | Producto, Stock, Almacen | Sí |
| RF-04 | Registrar y consultar información de producción | Produccion, Producto, Stock | Sí |
| RF-05 | Consultar existencias y registrar salidas de almacén | Almacen, Stock, Producto, Pedido | Sí |
| RF-06 | Consultar y actualizar el estado de los pedidos | Pedido | Sí |

---

## 3. Análisis de cobertura

Todos los requisitos funcionales identificados tienen al menos una clase relacionada.

Esto permite afirmar que no existen requisitos funcionales sin representación dentro del modelo conceptual.

También se verifica que las clases principales participan en uno o más requisitos.

### Cliente
Participa en RF-01 y RF-02.

### Pedido
Participa en RF-02, RF-05 y RF-06.

### Producto
Participa en RF-02, RF-03, RF-04 y RF-05.

### Stock
Participa en RF-03, RF-04 y RF-05.

### Produccion
Participa en RF-04.

### Almacen
Participa en RF-03 y RF-05.

### DetallePedido
Participa en RF-02.

---

## 4. Resultado

La matriz permite comprobar que existe trazabilidad entre los requisitos funcionales y las clases propuestas para Khanauky.

No se identifican clases completamente aisladas ni requisitos funcionales sin una clase asociada.

Esta información servirá como base para revisar el diagrama de clases UML y mantener consistencia entre los artefactos del proyecto.
