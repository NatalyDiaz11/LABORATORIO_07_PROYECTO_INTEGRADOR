# Stakeholders y catálogo de requisitos - Khanauky

## 1. Identificación de stakeholders

Los stakeholders son las personas o grupos que participan en el proceso, utilizan el sistema o se ven afectados por su funcionamiento.

| Stakeholder | Tipo | Interés principal |
|---|---|---|
| Vendedor | Primario | Registrar clientes y pedidos, consultar información y hacer seguimiento al estado de los pedidos. |
| Personal de Producción | Primario | Consultar los pedidos que requieren producción y registrar la información relacionada con el proceso productivo. |
| Personal de Almacén | Primario | Consultar existencias, registrar salidas de productos y mantener actualizado el stock. |
| Administrador o responsable del negocio | Primario | Supervisar la información de clientes, pedidos, producción, almacén y stock. |
| Cliente | Secundario | Recibir correctamente los productos solicitados y conocer el estado de su pedido. |

---

## 2. Catálogo de requisitos

| ID | Tipo | Descripción | Stakeholder principal | Prioridad |
|---|---|---|---|---|
| RF-01 | Funcional | El sistema debe permitir registrar y consultar información de los clientes. | Vendedor | Alta |
| RF-02 | Funcional | El sistema debe permitir registrar pedidos indicando el cliente, los productos y las cantidades solicitadas. | Vendedor | Alta |
| RF-03 | Funcional | El sistema debe permitir consultar y actualizar el stock disponible de los productos. | Almacén | Alta |
| RF-04 | Funcional | El sistema debe permitir registrar y consultar información de producción asociada a los pedidos. | Producción | Alta |
| RF-05 | Funcional | El sistema debe permitir consultar existencias y registrar las salidas de almacén asociadas a los pedidos. | Almacén | Alta |
| RF-06 | Funcional | El sistema debe permitir consultar y actualizar el estado de los pedidos. | Vendedor / Administrador | Alta |
| RNF-01 | No funcional - Usabilidad | El sistema debe presentar una interfaz clara y comprensible para sus usuarios. | Todos los usuarios | Media |
| RNF-02 | No funcional - Seguridad | El sistema debe permitir el acceso a la información únicamente a usuarios autorizados. | Administrador | Alta |
| RNF-03 | No funcional - Confiabilidad | El sistema debe mantener la consistencia de la información durante las operaciones de registro y actualización. | Todos los usuarios | Alta |
| RNF-04 | No funcional - Disponibilidad | El sistema debe mantener disponible la información necesaria durante las operaciones habituales del negocio. | Todos los usuarios | Media |

---

## 3. Relación entre stakeholders y requisitos

Cada requisito responde a una necesidad de uno o más stakeholders.

El vendedor necesita registrar clientes y pedidos; Producción requiere información de los pedidos que deben ser preparados; Almacén necesita controlar las existencias y las salidas de productos; y el administrador requiere supervisar la información general del negocio.

Esta relación permite comprobar que los requisitos definidos tienen una necesidad concreta dentro del proyecto Khanauky.
