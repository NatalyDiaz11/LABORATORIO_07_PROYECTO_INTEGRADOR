# Clases, responsabilidades, atributos y operaciones - Khanauky

## 1. Identificación de clases candidatas

A partir de los requisitos, casos de uso e historias de usuario definidos en los laboratorios anteriores, se identifican las siguientes clases principales para el sistema Khanauky:

- Cliente
- Pedido
- Producto
- Stock
- Produccion
- Almacen
- DetallePedido

Estas clases representan entidades y responsabilidades principales del sistema.

---

## 2. Clases y responsabilidades

| Clase | Responsabilidad principal |
|---|---|
| Cliente | Almacenar y gestionar la información de los clientes. |
| Pedido | Registrar y controlar la información general de los pedidos. |
| Producto | Representar los productos disponibles para la venta. |
| Stock | Controlar las cantidades disponibles de cada producto. |
| Produccion | Registrar información relacionada con los lotes y cantidades producidas. |
| Almacen | Gestionar existencias y salidas de productos. |
| DetallePedido | Relacionar un pedido con los productos y cantidades solicitadas. |

---

## 3. Atributos y operaciones

### Cliente

**Atributos**
- idCliente: int
- nombre: string
- documento: string
- telefono: string
- distrito: string

**Operaciones**
- registrar()
- consultar()
- actualizar()

---

### Pedido

**Atributos**
- idPedido: int
- fecha: date
- estado: string
- total: decimal

**Operaciones**
- registrar()
- atender()
- consultarEstado()
- actualizarEstado()

---

### Producto

**Atributos**
- idProducto: int
- nombre: string
- precio: decimal
- descripcion: string

**Operaciones**
- registrar()
- consultar()
- actualizar()

---

### Stock

**Atributos**
- idStock: int
- cantidadDisponible: int
- stockMinimo: int

**Operaciones**
- consultar()
- validarDisponibilidad()
- actualizar()
- verificarStockMinimo()
- generarAlertaStockMinimo()

---

### Produccion

**Atributos**
- idProduccion: int
- fechaProduccion: date
- cantidadProducida: int
- cantidadDefectuosa: int
- fechaVencimiento: date

**Operaciones**
- registrarProduccion()
- consultarProduccion()

---

### Almacen

**Atributos**
- idAlmacen: int
- nombre: string
- ubicacion: string

**Operaciones**
- consultarExistencias()
- registrarSalida()
- actualizarExistencias()

---

### DetallePedido

**Atributos**
- idDetalle: int
- cantidad: int
- precioUnitario: decimal
- subtotal: decimal

**Operaciones**
- calcularSubtotal()
- registrarDetalle()

---

## 4. Justificación del modelo

Las clases identificadas permiten representar las principales responsabilidades del sistema Khanauky.

Cliente y Pedido representan la información relacionada con la atención de ventas.

Producto, Stock y Almacen permiten controlar la disponibilidad y movimiento de productos.

Produccion permite registrar los lotes elaborados.

DetallePedido permite separar la información general del pedido de los productos y cantidades específicas que lo componen.

Esta separación mejora la organización de responsabilidades y facilita mantener una alta cohesión dentro de cada clase.

---

## 5. Convenciones utilizadas

- Los nombres de clases se escriben en PascalCase.
- Los atributos y operaciones utilizan camelCase.
- Los atributos se consideran privados.
- Las operaciones principales se consideran públicas.
- Cada clase debe tener una responsabilidad claramente definida.

---

## Resultado

La identificación de clases, atributos y operaciones permite transformar los requisitos y casos de uso del proyecto Khanauky en una estructura conceptual que posteriormente será representada mediante un diagrama de clases UML.
