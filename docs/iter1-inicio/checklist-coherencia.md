# Checklist de coherencia - Khanauky

Se realizó la revisión de coherencia entre el Documento de Visión, roadmap, matriz fase-artefacto, actividad del proceso crítico, glosario, riesgos y convenciones del proyecto.

| # | Verificación | Resultado | Observación |
|---|---|---|---|
| 1 | Los actores utilizan el mismo nombre en todos los documentos. | ✅ Verificado | Verificado en vision.md, glosario.md y actividad-atender-pedido.md. |
| 2 | Cada requisito de la Visión tiene relación con una función o caso de uso del sistema. | ✅ Verificado | REQ-001 a REQ-006 se relacionan con cliente, pedido, stock, producción, almacén y estado del pedido. |
| 3 | El proceso Atender pedido aparece de forma coherente en Visión, roadmap, matriz y actividad. | ✅ Verificado | Verificado en vision.md, roadmap.md, matriz-fase-artefacto.md y actividad-atender-pedido.md. |
| 4 | Las excepciones del proceso están representadas en la actividad. | ✅ Verificado | Verificado en actividad-atender-pedido.md mediante E1, E2, E3 y E4. |
| 5 | La compensación C1 está representada en la actividad. | ✅ Verificado | Verificado en actividad-atender-pedido.md mediante la restauración de valores o el estado Pendiente de revisión. |
| 6 | Ninguna funcionalidad modelada está fuera del alcance definido en la Visión. | ✅ Verificado | Verificado en vision.md y actividad-atender-pedido.md. No se incluyeron contabilidad completa, recursos humanos, GPS ni integración bancaria. |
| 7 | Producción y Almacén se mantienen como funciones diferentes. | ✅ Verificado | Verificado en vision.md, glosario.md y actividad-atender-pedido.md. |
| 8 | El término Pedido se usa de manera diferente al término Venta. | ✅ Verificado | Verificado en glosario.md. Pedido y Venta se mantienen como conceptos distintos. |
| 9 | El pedido solo se confirma después de una actualización correcta del stock. | ✅ Verificado | Verificado en actividad-atender-pedido.md y en el diagrama Mermaid corregido. |
| 10 | El estado del pedido permanece identificable durante todo el proceso. | ✅ Verificado | Verificado en actividad-atender-pedido.md mediante estados como pendiente, pendiente de producción, pendiente de revisión y atendido. |
| 11 | Los IDs siguen las convenciones REQ-###, CU-###, RSK-### e ITER-#. | ✅ Verificado | CU-002 corresponde a Atender pedido y las convenciones se encuentran definidas en 00-convenciones.md. |
| 12 | Los nombres utilizados coinciden con el glosario oficial. | ✅ Verificado | Cliente, Vendedor, Pedido, Stock, Producción y Almacén mantienen los términos definidos en glosario.md. |

## Hallazgos encontrados

| # | Hallazgo | Corrección aplicada | Estado |
|---|---|---|---|
| 1 | El proceso Atender pedido estaba identificado inicialmente sin seguir completamente la convención CU-###. | Se estableció el identificador CU-002 - Atender pedido. | Corregido |
| 2 | La confirmación del pedido aparecía antes de la actualización del stock. | Se modificó el flujo para que el stock se actualice correctamente antes de confirmar definitivamente el pedido. | Corregido |
| 3 | Existía una diferencia entre el orden del flujo textual y el diagrama Mermaid. | Se unificó el orden del flujo principal y el diagrama. | Corregido |
| 4 | Las responsabilidades de Producción y Almacén podían interpretarse como una sola función. | Se definieron responsabilidades independientes para Producción y Almacén. | Corregido |

## Resultado final

La revisión permitió comprobar que los principales artefactos de la ITER-1 mantienen coherencia entre alcance, requisitos, terminología, proceso crítico y riesgos.

Los hallazgos identificados fueron corregidos antes del cierre de la iteración.


Los hallazgos identificados fueron corregidos antes del cierre de la iteración.
