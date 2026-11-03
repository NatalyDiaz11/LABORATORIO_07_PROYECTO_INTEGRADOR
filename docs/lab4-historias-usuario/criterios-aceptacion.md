# Criterios de aceptación - Khanauky

## HU-01 - Registrar cliente

### Criterio 1
**Dado que** el vendedor necesita registrar un nuevo cliente,  
**Cuando** ingresa correctamente los datos obligatorios y confirma el registro,  
**Entonces** el sistema guarda la información del cliente y muestra una confirmación.

### Criterio 2
**Dado que** faltan datos obligatorios del cliente,  
**Cuando** el vendedor intenta confirmar el registro,  
**Entonces** el sistema muestra un aviso y solicita completar la información.

### Criterio 3
**Dado que** el cliente ya se encuentra registrado,  
**Cuando** el vendedor intenta registrarlo nuevamente,  
**Entonces** el sistema informa que el cliente ya existe.

---

## HU-02 - Registrar pedido

### Criterio 1
**Dado que** el cliente se encuentra registrado,  
**Cuando** el vendedor selecciona productos, ingresa cantidades válidas y confirma,  
**Entonces** el sistema registra el pedido con estado Pendiente.

### Criterio 2
**Dado que** no se han seleccionado productos o cantidades,  
**Cuando** el vendedor intenta registrar el pedido,  
**Entonces** el sistema muestra un mensaje de validación y no completa el registro.

### Criterio 3
**Dado que** falta información obligatoria del pedido,  
**Cuando** el vendedor intenta confirmar el registro,  
**Entonces** el sistema solicita completar los datos antes de continuar.

---

## HU-03 - Consultar y actualizar stock

### Criterio 1
**Dado que** el producto se encuentra registrado,  
**Cuando** el personal de Almacén consulta el producto,  
**Entonces** el sistema muestra la cantidad disponible registrada.

### Criterio 2
**Dado que** se registra una cantidad válida,  
**Cuando** el personal de Almacén confirma la actualización,  
**Entonces** el sistema actualiza el stock y muestra la nueva cantidad disponible.

### Criterio 3
**Dado que** se intenta ingresar una cantidad negativa,  
**Cuando** el usuario confirma la actualización,  
**Entonces** el sistema rechaza el valor y muestra un mensaje de error.

---

## HU-04 - Registrar producción

### Criterio 1
**Dado que** el personal de Producción desea registrar un nuevo lote,  
**Cuando** selecciona el producto, registra las unidades producidas y completa los datos obligatorios,  
**Entonces** el sistema guarda el lote de producción.

### Criterio 2
**Dado que** se registraron unidades defectuosas,  
**Cuando** se confirma el lote,  
**Entonces** el sistema conserva la información de unidades producidas y defectuosas.

### Criterio 3
**Dado que** falta información obligatoria del lote,  
**Cuando** el usuario intenta registrarlo,  
**Entonces** el sistema solicita completar los datos antes de guardar.

---

## HU-05 - Consultar estado del pedido

### Criterio 1
**Dado que** existe un pedido registrado,  
**Cuando** el vendedor consulta su información,  
**Entonces** el sistema muestra su estado actual.

### Criterio 2
**Dado que** el estado del pedido cambia durante su atención,  
**Cuando** el sistema registra el nuevo estado,  
**Entonces** la información actualizada queda disponible para su consulta.

### Criterio 3
**Dado que** el pedido fue entregado,  
**Cuando** se consulta nuevamente,  
**Entonces** el sistema muestra el estado Entregado.

---

## Resultado

Los criterios de aceptación permiten definir de manera clara cómo se comprobará que cada historia de usuario cumple con el comportamiento esperado.

El formato Dado que / Cuando / Entonces facilita la validación de cada funcionalidad antes de considerarla terminada.
