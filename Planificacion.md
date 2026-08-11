# Objetivo del proyecto

Desarrollar una aplicación web para la gestión y análisis de una cartera de inversiones personales.

La aplicación se construirá por etapas, priorizando primero un backend sólido, luego un dashboard de análisis y finalmente herramientas avanzadas de gestión e integración con datos de mercado.

## Sprint 1 - Dashboard principal

- ✅ Crear tarjetas históricas por activo.
- ✅ Mostrar ganancia realizada por activo.
- ✅ Mostrar rentabilidad histórica por activo.

---

## Sprint 2 - Resumen por activo

- ✅ Mostrar cantidad actual.
- ✅ Mostrar PPC.
- ✅ Mostrar capital invertido.
- [ ] Mostrar valor actual.
- [ ] Mostrar rentabilidad.
- [ ] Mostrar ganancia no realizada.

---

## Sprint 3 - Posiciones abiertas

- ✅ Mejorar formato de números.
- [ ] Agregar acciones sobre las posiciones.
- ✅ Mostrar detalle de una posición.

---

## Sprint 4 - Detalle de posición

- ✅ Mostrar resumen de la posición en caso de existir abierta para registrar una compra.
- ✅ Mostrar resumen de la posición para registrar una venta.
- ✅ Mejorar la interacción del usuario después de cada operación.
- ✅ Mostrar métricas completas.

---

## Sprint 5 - Validación y consistencia de datos

- [ ] Validar que las operaciones mantengan una posición consistente.
- [ ] Validar cantidades después de compras y ventas.
- [ ] Validar que no se pueda operar sobre una posición cerrada.
- [ ] Validar estados de las posiciones.
- [ ] Revisar casos límite de ventas parciales y totales.
- [ ] Evitar que una operación inválida modifique los datos.
- [ ] Revisar y centralizar validaciones repetidas.

---

## Sprint 6 - Navegación y acciones sobre posiciones

- [ ] Agregar acciones sobre las posiciones abiertas.
- [ ] Acceder al detalle desde las posiciones.
- [ ] Eliminar posiciones.
- [ ] Validar eliminación únicamente cuando corresponda.
- [ ] Actualizar automáticamente el Dashboard.
- [ ] Permitir consultar posiciones finalizadas.

---

## Sprint 7 - Gestión de Operaciones

- [ ] Editar operaciones.
- [ ] Eliminar operaciones.
- [ ] Recalcular resumen de la posición después de editar.
- [ ] Recalcular resumen de la posición después de eliminar.
- [ ] Mantener consistencia de la posición después de una modificación.

---

## Sprint 8 - Historial

- [ ] Pantalla de posiciones cerradas.
- [ ] Ver detalle de una posición cerrada.
- [ ]  Diferenciar visualmente posiciones abiertas y cerradas.

---

## Sprint 9 - Operaciones

- [ ] Historial completo de operaciones.
- [ ] Filtros por activo.
- [ ] Filtros por fecha.

---

## Sprint 10 - Persistencia

- [ ] Migrar de JSON a SQLite.

---

## Sprint 11 - Integraciones

- [ ] Integrar API de precios.
- [ ] Actualizar valor de mercado automáticamente.