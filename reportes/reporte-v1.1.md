# Reporte de trazabilidad v1.1 - Khanauky

## 1. Resumen

La versión v1.1 del proyecto Khanauky incorpora el cambio controlado CR-001, relacionado con la generación de una alerta de stock mínimo durante la atención de pedidos.

El cambio fue aplicado sobre la línea base v1.0 y afectó requisitos, casos de uso, pruebas, modelo de clases y matriz de trazabilidad.

---

## 2. Cambio aplicado

**ID del cambio:** CR-001

**Nombre:** Alerta de stock mínimo al atender un pedido

**Requisito afectado:** REQ-003

**Descripción:**
Cuando se atiende un pedido y se actualiza el stock, el sistema verifica la cantidad disponible. Si esta queda por debajo del stock mínimo definido, se genera una alerta para Almacén.

**Decisión:** Aprobado

---

## 3. Artefactos modificados

Los siguientes artefactos fueron actualizados como consecuencia del CR-001:

- SRS.md
- CU.md
- pruebas.md
- clases.drawio
- clases.png
- trazabilidad.md

---

## 4. Requisitos modificados

| Requisito | Estado | Cambio |
|---|---|---|
| REQ-001 | Sin cambios | - |
| REQ-002 | Sin cambios | - |
| REQ-003 | Modificado | Se agregó la generación de una alerta cuando el stock queda por debajo del mínimo definido |
| REQ-004 | Sin cambios | - |
| REQ-005 | Sin cambios | - |
| REQ-006 | Sin cambios | - |

---

## 5. Pruebas asociadas al cambio

Para validar el cambio se mantienen y agregan las siguientes pruebas:

- PRU-003: consultar y actualizar el stock de un producto.
- PRU-003a: actualizar el stock manteniéndolo por encima o igual al mínimo definido.
- PRU-003b: actualizar el stock dejándolo por debajo del mínimo definido y comprobar la generación de la alerta.
- PRU-003c: atender un pedido con un producto sin stock mínimo configurado y comprobar que el sistema informe la condición, permita continuar y no genere la alerta.

Estado de ejecución de pruebas: Pendiente.

---

## 6. Cobertura de trazabilidad

Requisitos totales: 6

Requisitos con prueba asociada: 6

Cobertura de trazabilidad: 100 %

El 100 % representa que todos los requisitos tienen al menos una prueba asociada. No representa que todas las pruebas hayan sido ejecutadas exitosamente.

---

## 7. Trazabilidad del cambio

REQ-003 → CU-002 → CLS-Stock → PRU-003 / PRU-003a / PRU-003b → CR-001

---

## 8. Comparación entre v1.0 y v1.1

### v1.0
La línea base inicial incluía el registro y actualización de stock, pero no contemplaba una alerta cuando las existencias quedaban por debajo de un nivel mínimo.

### v1.1
Se incorpora el control de stock mínimo y la generación de una alerta para Almacén, manteniendo la trazabilidad entre requisito, caso de uso, clase y pruebas.

---

## 9. Conclusión

El CR-001 fue incorporado de forma controlada y trazable. El cambio afecta principalmente al control de stock y permite identificar existencias bajas durante la atención de pedidos.

La actualización conserva la cobertura de trazabilidad del 100 % y permite identificar claramente los artefactos afectados por el cambio.
