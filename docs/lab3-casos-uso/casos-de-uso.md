# Especificación de casos de uso - Khanauky

## CU-001: Gestionar clientes

### Actor principal
Vendedor

### Precondición
El vendedor debe tener acceso al sistema.

### Postcondición
La información del cliente queda registrada o disponible para consulta.

### Flujo principal
1. El vendedor ingresa a la opción de gestión de clientes.
2. El sistema muestra las opciones disponibles.
3. El vendedor registra los datos del cliente.
4. El sistema valida que la información obligatoria esté completa.
5. El sistema guarda la información.
6. El sistema confirma el registro del cliente.

### Excepciones
- E1: Si faltan datos obligatorios, el sistema solicita completar la información.
- E2: Si el cliente ya existe, el sistema informa que ya se encuentra registrado.

### Regla de negocio
No se debe registrar dos veces al mismo cliente con la misma información de identificación.

---

## CU-002: Atender pedido

### Actor principal
Vendedor

### Actores relacionados
Cliente, Producción y Almacén.

### Precondición
El pedido debe estar previamente registrado y encontrarse en estado Pendiente.

### Postcondición
El pedido queda atendido y el stock registrado se actualiza según los productos entregados.

### Flujo principal
1. El vendedor selecciona un pedido pendiente.
2. El sistema muestra la información del cliente y el detalle del pedido.
3. El vendedor revisa los productos y cantidades solicitadas.
4. El sistema consulta la disponibilidad de stock.
5. Si se requiere producción adicional, se coordina con Producción.
6. Almacén confirma la salida de los productos correspondientes.
7. El sistema descuenta las cantidades entregadas y actualiza el stock.
8. El sistema confirma que la atención del pedido fue realizada correctamente.
9. El estado del pedido cambia a Atendido.
10. El sistema muestra la confirmación final.

### Flujos alternos
- A1: Si no existe stock suficiente, el pedido permanece pendiente hasta disponer de los productos necesarios.
- A2: Si se requiere producción, el pedido continúa una vez que los productos estén disponibles.

### Excepciones
- E1: Stock insuficiente.
- E2: Error durante la actualización del stock.
- E3: Información del cliente incompleta.
- E4: Pedido no disponible para atención.

### Reglas de negocio
- Un pedido solo puede pasar a Atendido cuando se haya confirmado la entrega de los productos correspondientes.
- La cantidad entregada debe descontarse del stock registrado.

---

## CU-003: Registrar pedido

### Actor principal
Vendedor

### Actor relacionado
Cliente

### Precondición
El cliente debe encontrarse registrado en el sistema.

### Postcondición
El pedido queda registrado con estado Pendiente.

### Flujo principal
1. El vendedor identifica o selecciona al cliente.
2. El sistema muestra la información del cliente.
3. El vendedor registra los productos solicitados.
4. El vendedor registra las cantidades de cada producto.
5. El sistema valida que la información obligatoria esté completa.
6. El sistema registra el pedido.
7. El pedido queda con estado Pendiente.
8. El sistema muestra la confirmación del registro.

### Flujos alternos
- A1: Si el cliente no existe, el vendedor debe registrarlo antes de continuar.

### Excepciones
- E1: Faltan datos obligatorios.
- E2: No se han registrado productos o cantidades.
- E3: Ocurre un error durante el registro del pedido.

### Reglas de negocio
- Todo pedido debe estar asociado a un cliente registrado.
- Todo pedido nuevo debe iniciar con estado Pendiente.

---

## CU-004: Consultar y actualizar stock

### Actor principal
Personal de Almacén

### Precondición
El producto debe encontrarse registrado.

### Postcondición
La información del stock queda consultada o actualizada.

### Flujo principal
1. El personal de Almacén selecciona el producto.
2. El sistema muestra la cantidad disponible.
3. El usuario registra la nueva cantidad cuando corresponde.
4. El sistema valida el valor ingresado.
5. El sistema actualiza el stock.
6. El sistema confirma la operación.

### Excepciones
- E1: Producto no encontrado.
- E2: Cantidad ingresada no válida.

### Regla de negocio
El stock registrado no debe quedar con valores negativos.
