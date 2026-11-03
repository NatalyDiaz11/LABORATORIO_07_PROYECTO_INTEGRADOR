# Reglas de negocio, validaciones y excepciones - Khanauky

## 1. Matriz de reglas de negocio

| ID | Regla | Caso de uso relacionado | Tipo |
|---|---|---|---|
| RN-01 | Todo pedido debe estar asociado a un cliente registrado. | CU-003 Registrar pedido | Validación |
| RN-02 | Todo pedido nuevo debe iniciar con estado Pendiente. | CU-003 Registrar pedido | Regla de negocio |
| RN-03 | Un pedido solo puede pasar a Atendido cuando se haya confirmado la entrega de los productos correspondientes. | CU-002 Atender pedido | Regla de negocio |
| RN-04 | Antes de atender un pedido, el sistema debe verificar la disponibilidad de stock. | CU-002 Atender pedido / CU-004 Consultar y actualizar stock | Validación |
| RN-05 | La cantidad entregada debe descontarse del stock registrado. | CU-002 Atender pedido | Regla de negocio |
| RN-06 | El stock registrado no debe quedar con valores negativos. | CU-004 Consultar y actualizar stock | Validación |
| RN-07 | Si no existe stock suficiente, el pedido debe permanecer pendiente hasta contar con los productos necesarios. | CU-002 Atender pedido | Excepción |
| RN-08 | Si se requiere producción adicional, el pedido continuará su atención cuando los productos estén disponibles. | CU-002 Atender pedido / CU-005 Registrar producción | Regla de negocio |
| RN-09 | La salida de productos de Almacén debe quedar asociada al pedido correspondiente. | CU-006 Registrar salida de almacén | Validación |
| RN-10 | El estado del pedido debe reflejar la etapa real de su atención. | CU-007 Consultar estado del pedido | Regla de negocio |

---

## 2. Validaciones principales

Las principales validaciones del sistema son:

- Verificar que el cliente esté registrado antes de crear un pedido.
- Verificar que el pedido tenga productos y cantidades válidas.
- Verificar la disponibilidad de stock antes de confirmar la atención.
- Evitar cantidades negativas en el stock.
- Confirmar la salida de productos antes de cambiar el pedido a estado Atendido.
- Mantener actualizado el estado del pedido según el avance real del proceso.

---

## 3. Excepciones principales

Durante la operación del sistema pueden presentarse las siguientes excepciones:

- Cliente no registrado.
- Información obligatoria incompleta.
- Producto no encontrado.
- Stock insuficiente.
- Error durante la actualización del stock.
- Pedido no disponible para atención.
- Error durante el registro de la salida de almacén.

---

## 4. Relación con los casos de uso

Las reglas de negocio permiten mantener consistencia entre los distintos casos de uso.

Por ejemplo, CU-003 registra un pedido con estado Pendiente y CU-002 permite atenderlo posteriormente, siempre que se cumplan las validaciones de stock y salida de productos.

De esta manera se evita que los casos de uso funcionen de forma aislada o contradictoria.# Reglas de negocio, validaciones y excepciones - Khanauky

## 1. Matriz de reglas de negocio

| ID | Regla | Caso de uso relacionado | Tipo |
|---|---|---|---|
| RN-01 | Todo pedido debe estar asociado a un cliente registrado. | CU-003 Registrar pedido | Validación |
| RN-02 | Todo pedido nuevo debe iniciar con estado Pendiente. | CU-003 Registrar pedido | Regla de negocio |
| RN-03 | Un pedido solo puede pasar a Atendido cuando se haya confirmado la entrega de los productos correspondientes. | CU-002 Atender pedido | Regla de negocio |
| RN-04 | Antes de atender un pedido, el sistema debe verificar la disponibilidad de stock. | CU-002 Atender pedido / CU-004 Consultar y actualizar stock | Validación |
| RN-05 | La cantidad entregada debe descontarse del stock registrado. | CU-002 Atender pedido | Regla de negocio |
| RN-06 | El stock registrado no debe quedar con valores negativos. | CU-004 Consultar y actualizar stock | Validación |
| RN-07 | Si no existe stock suficiente, el pedido debe permanecer pendiente hasta contar con los productos necesarios. | CU-002 Atender pedido | Excepción |
| RN-08 | Si se requiere producción adicional, el pedido continuará su atención cuando los productos estén disponibles. | CU-002 Atender pedido / CU-005 Registrar producción | Regla de negocio |
| RN-09 | La salida de productos de Almacén debe quedar asociada al pedido correspondiente. | CU-006 Registrar salida de almacén | Validación |
| RN-10 | El estado del pedido debe reflejar la etapa real de su atención. | CU-007 Consultar estado del pedido | Regla de negocio |

---

## 2. Validaciones principales

Las principales validaciones del sistema son:

- Verificar que el cliente esté registrado antes de crear un pedido.
- Verificar que el pedido tenga productos y cantidades válidas.
- Verificar la disponibilidad de stock antes de confirmar la atención.
- Evitar cantidades negativas en el stock.
- Confirmar la salida de productos antes de cambiar el pedido a estado Atendido.
- Mantener actualizado el estado del pedido según el avance real del proceso.

---

## 3. Excepciones principales

Durante la operación del sistema pueden presentarse las siguientes excepciones:

- Cliente no registrado.
- Información obligatoria incompleta.
- Producto no encontrado.
- Stock insuficiente.
- Error durante la actualización del stock.
- Pedido no disponible para atención.
- Error durante el registro de la salida de almacén.

---

## 4. Relación con los casos de uso

Las reglas de negocio permiten mantener consistencia entre los distintos casos de uso.

Por ejemplo, CU-003 registra un pedido con estado Pendiente y CU-002 permite atenderlo posteriormente, siempre que se cumplan las validaciones de stock y salida de productos.

De esta manera se evita que los casos de uso funcionen de forma aislada o contradictoria.
