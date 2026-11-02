# Validación de requisitos y resolución de conflictos - Khanauky

## 1. Validación de requisitos

Para validar los requisitos del sistema Khanauky se realizó una revisión guiada de los requerimientos funcionales con representantes de las áreas de ventas y almacén.

Durante la revisión se verificó que los requisitos relacionados con registro de pedidos, control de stock, producción, almacén y consulta del estado del pedido respondieran a necesidades reales del negocio.

Como resultado, los participantes confirmaron que los requisitos definidos representan adecuadamente las funciones principales que debe cubrir el sistema.

---

## 2. Conflicto entre stakeholders

### Stakeholder 1: Vendedor

El vendedor considera importante que un pedido pueda registrarse y continuar su atención rápidamente para evitar demoras al cliente.

### Stakeholder 2: Personal de Almacén

El personal de Almacén considera que antes de confirmar la atención de un pedido debe verificarse que exista stock suficiente para evitar diferencias entre las existencias reales y las registradas.

### Conflicto identificado

El conflicto se presenta entre la rapidez en la atención del pedido y la necesidad de verificar correctamente la disponibilidad de stock antes de continuar.

---

## 3. Opciones de solución

### Opción A

Permitir que el vendedor continúe con la atención del pedido sin realizar una validación previa de stock.

### Opción B

Realizar una verificación automática del stock antes de confirmar la atención del pedido y permitir que el proceso continúe cuando exista disponibilidad suficiente.

---

## 4. Matriz de decisión

Se utiliza una escala de 1 a 5, donde 1 representa una valoración baja y 5 una valoración alta.

| Criterio | Peso | Opción A | Opción B |
|---|---:|---:|---:|
| Rapidez de atención | 30 % | 5 | 4 |
| Confiabilidad de la información | 40 % | 2 | 5 |
| Control de stock | 30 % | 1 | 5 |

### Resultado

**Opción A**

(5 × 0.30) + (2 × 0.40) + (1 × 0.30)

= 1.50 + 0.80 + 0.30

= **2.60**

**Opción B**

(4 × 0.30) + (5 × 0.40) + (5 × 0.30)

= 1.20 + 2.00 + 1.50

= **4.70**

---

## 5. Decisión final

Se selecciona la **Opción B**, debido a que obtiene el mayor puntaje.

La verificación automática del stock permite mantener la confiabilidad de la información y reducir el riesgo de atender pedidos con productos no disponibles, sin impedir que el proceso continúe cuando exista stock suficiente.

Esta decisión se relaciona directamente con el requisito de control de stock del proyecto Khanauky.
