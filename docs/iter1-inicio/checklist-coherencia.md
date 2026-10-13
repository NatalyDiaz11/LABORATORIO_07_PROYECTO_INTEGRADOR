## Checklist de coherencia - Khanauky

Se realizó la revisión de coherencia entre el Documento de Visión, roadmap, matriz fase-artefacto, actividad del proceso crítico, glosario, riesgos y convenciones del proyecto.

| # | Verificación | Resultado | Observación |
|---|---|---|---|
| 1 | Los actores utilizan el mismo nombre en todos los documentos. | ✅ Verificado | Se mantienen de forma consistente Cliente, Vendedor, Producción, Almacén y Administrador. |
| 2 | Cada requisito de la Visión tiene relación con una función o caso de uso del sistema. | ✅ Verificado | REQ-001 a REQ-006 están relacionados con cliente, pedido, stock, producción, almacén y estado del pedido. |
| 3 | El proceso Atender pedido aparece de forma coherente en Visión, roadmap, matriz y actividad. | ✅ Verificado | Se utiliza Atender pedido como proceso crítico y no Registrar venta como proceso principal. |
| 4 | Las excepciones del proceso están representadas en la actividad. | ✅ Verificado | Se contemplan E1 Cliente no registrado, E2 Stock insuficiente, E3 Producto requiere producción y E4 Error al actualizar stock. |
| 5 | La compensación C1 está representada en la actividad. | ✅ Verificado | Ante un error se restaura la información anterior o se deja el pedido pendiente de revisión. |
| 6 | Ninguna funcionalidad modelada está fuera del alcance definido en la Visión. | ✅ Verificado | No se incluyeron contabilidad completa, recursos humanos, GPS, integración bancaria ni otras funciones fuera del alcance. |
| 7 | Producción y Almacén se mantienen como funciones diferentes. | ✅ Verificado | Ambas responsabilidades permanecen diferenciadas aunque una misma persona pueda cumplirlas. |
| 8 | El término Pedido se usa de manera diferente al término Venta. | ✅ Verificado | El glosario establece que Pedido y Venta representan conceptos diferentes. |
| 9 | El stock solo se actualiza después de confirmar correctamente la atención del pedido. | ✅ Verificado | En el flujo se confirma la atención antes de realizar la actualización final del stock. |
| 10 | El estado del pedido permanece identificable durante todo el proceso. | ✅ Verificado | Se contemplan situaciones como pendiente, pendiente de producción, pendiente de revisión y atendido. |
| 11 | Los IDs siguen las convenciones REQ-###, CU-###, RSK-### e ITER-#. | ✅ Corregido | Se detectó que Atender pedido no tenía numeración de CU. Se corrigió a CU-002. |
| 12 | Los nombres utilizados coinciden con el glosario oficial. | ✅ Verificado | Cliente, Vendedor, Pedido, Stock, Producción y Almacén mantienen los términos definidos en el glosario. |

## Hallazgos encontrados

| # | Hallazgo | Corrección aplicada | Estado |
|---|---|---|---|
| 1 | El proceso Atender pedido estaba identificado como "CU - Atender pedido" sin seguir la convención CU-###. | Se asignó el identificador CU-002, quedando como "CU-002 - Atender pedido". | Corregido |
| 2 | En una versión inicial se consideró Registrar venta como proceso principal. | Se unificó el proceso crítico bajo Atender pedido para mantener coherencia con el alcance de Khanauky. | Corregido |
| 3 | Existía el riesgo de representar Producción y Almacén como una sola función debido a que una misma persona puede asumir ambas responsabilidades. | Se mantuvieron Producción y Almacén como funciones independientes en el modelado. | Corregido |

## Resultado final

La revisión permitió comprobar que los principales artefactos de la ITER-1 mantienen coherencia entre alcance, requisitos, terminología, proceso crítico y riesgos.

Los hallazgos identificados fueron corregidos antes del cierre de la iteración.
