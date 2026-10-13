# Revisión por pares - ITER-1 Khanauky

Este documento registra la revisión realizada sobre los artefactos de la ITER-1 antes de su integración a la rama principal.

## Datos de la revisión

- Revisor: Lilaltz
- Fecha: 13/10/2026
- Pull Request: #1 - ITER1: planificación de la fase de Inicio - Khanauky

## Checklist para el revisor

| # | Pregunta | Sí / No | Observación |
|---|---|---|---|
| 1 | ¿La Visión indica claramente qué incluye y qué no incluye? | Sí | Se identificó la necesidad de precisar quién registra el pedido y mejorar los objetivos medibles. |
| 2 | ¿El roadmap contiene objetivo, entregables, responsable y plazo para cada iteración? | Sí | La estructura se mantiene coherente con las cuatro fases RUP. |
| 3 | ¿La matriz fase-artefacto es coherente con el roadmap? | Sí | Los artefactos corresponden a las fases planteadas. |
| 4 | ¿El proceso Atender pedido presenta flujo principal y excepciones? | Sí | Se revisó el orden del flujo y se corrigió para que coincida con el diagrama Mermaid. |
| 5 | ¿Las excepciones E1, E2, E3 y E4 están correctamente representadas? | Sí | Las excepciones se mantienen dentro del proceso crítico. |
| 6 | ¿La compensación C1 evita inconsistencias entre pedido y stock? | Sí | Se precisó que la restauración se realiza cuando sea segura; de lo contrario, el pedido queda pendiente de revisión. |
| 7 | ¿Los términos usados coinciden con el glosario? | Sí | Se mantiene diferenciación entre Pedido, Venta, Producción, Almacén y Stock. |
| 8 | ¿Producción y Almacén permanecen como funciones diferentes? | Sí | Se aclararon sus responsabilidades por separado. |
| 9 | ¿Cada riesgo tiene mitigación y responsable? | Sí | Se añadieron criterios de probabilidad e impacto y se precisó la mitigación de RSK-005. |
| 10 | ¿Los IDs y nombres de archivos siguen las convenciones del proyecto? | Sí | CU-002 se mantiene asociado a Atender pedido. |
| 11 | ¿El proceso Atender pedido mantiene coherencia con la Visión y los requisitos? | Sí | Se corrigió la secuencia entre actualización de stock y confirmación del pedido. |
| 12 | ¿El estado del pedido permanece identificable durante todo el proceso? | Sí | Se mantienen estados como pendiente, pendiente de producción, pendiente de revisión y atendido. |

## Hallazgos de la revisión

| # | Hallazgo | Corrección aplicada | Estado |
|---|---|---|---|
| 1 | La confirmación del pedido se realizaba antes de completar correctamente la actualización del stock. | Se modificó el flujo para actualizar primero el stock y confirmar el pedido solo si la operación termina correctamente. | Corregido |
| 2 | El flujo textual y el diagrama Mermaid no seguían exactamente el mismo orden. | Se unificó la secuencia de ambos artefactos. | Corregido |
| 3 | Las responsabilidades de Producción y Almacén requerían mayor precisión. | Se definieron responsabilidades independientes para ambas funciones. | Corregido |
| 4 | La compensación C1 no especificaba cuándo restaurar información o cuándo dejar el pedido pendiente. | Se definió restauración cuando sea segura y estado Pendiente de revisión cuando no pueda garantizarse la consistencia. | Corregido |
| 5 | Los objetivos de la Visión no eran suficientemente medibles. | Se reformularon utilizando criterios verificables relacionados con pedidos, stock y estados. | Corregido |
| 6 | No estaba completamente claro quién registra el pedido en el sistema. | Se aclaró que el cliente realiza la solicitud y el vendedor registra o gestiona el pedido. | Corregido |
| 7 | La actualización manual y automática del stock no estaba diferenciada. | Se indicó que la atención del pedido genera actualización asociada y que Almacén puede realizar ingresos, reposiciones o ajustes manuales. | Corregido |
| 8 | La tabla de riesgos no explicaba cómo se asignaban probabilidad e impacto. | Se agregaron criterios de evaluación para ambos campos. | Corregido |
| 9 | El checklist de coherencia necesitaba mayor trazabilidad. | Se añadieron referencias a los archivos donde se verificó cada criterio. | Corregido |

## Estados utilizados

- Pendiente: el hallazgo fue identificado pero aún no se ha atendido.
- En revisión: se realizó una modificación y todavía debe comprobarse.
- Corregido: la modificación fue revisada y comprobada en el artefacto actualizado.

## Cierre de revisión

- [x] Los comentarios del revisor fueron revisados.
- [x] Las correcciones necesarias fueron incorporadas.
- [x] El checklist de coherencia fue actualizado.
- [x] Los artefactos modificados fueron verificados nuevamente.
- [x] La iteración está lista para integrarse a la rama principal.

Una corrección solo se considera cerrada después de comprobar el cambio directamente en el archivo actualizado.
