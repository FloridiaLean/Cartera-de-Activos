# Registro de compras

- Compra válida.
- Compra válida desde el menú principal.
- Monto de inversión negativo.
- Monto de inversión igual a 0.
- Precio de compra negativo.
- Precio de compra igual a 0.
- Activo vacío.
- Fecha de compra válida.
- Intentar registrar una compra con una fecha anterior a una operación ya registrada.
- Agregar compra a una posición existente desde el flujo independiente.
- Crear una nueva posición para el mismo activo desde el flujo independiente.
- Agregar compra directamente desde una posición abierta en el Dashboard.
- Verificar que la compra contextual se agregue a la posición seleccionada.
- Volver al Dashboard después de registrar una compra contextual.
- Mantener el flujo independiente de compra sin modificaciones.

# Registro de ventas

- Venta válida.
- Venta válida desde el menú principal.
- Venta mayor a la cantidad disponible.
- Venta igual a la cantidad disponible.
- Venta de un activo inexistente.
- Venta sin posiciones abiertas.
- Cantidad de venta negativa.
- Cantidad de venta igual a 0.
- Fecha de venta válida.
- Intentar registrar una venta con una fecha anterior a una operación ya registrada.
- Registrar una venta parcial desde una posición del Dashboard.
- Registrar una venta desde el flujo independiente.
- Utilizar el botón Max para cargar toda la cantidad disponible.
- Verificar que Max cargue la cantidad correspondiente a la posición seleccionada.
- Verificar que el botón Max no afecte la cantidad de otra posición.
- Cierre automático de la posición al vender el total.
- Volver al Dashboard después de registrar una venta contextual.
- Volver al Dashboard cuando una venta contextual falla por una validación.
- Mantener el flujo independiente de venta sin modificaciones.

# Edición de operaciones

- Editar una compra.
- Editar una compra con ventas asociadas.
- Editar una venta.
- Reapertura automática de la posición al editar una venta.
- Seleccionar una operación inexistente.
- Intentar editar sin operaciones registradas.
- Verificar que la edición de una operación no permita modificar su fecha.
- Verificar que las cantidades y valores resultantes sean correctos después de editar.

# Eliminación de operaciones

- Eliminar una venta.
- Eliminar una compra sin ventas asociadas.
- No permitir eliminar una compra con ventas asociadas.
- Eliminar la última operación de una posición.
- Eliminar una operación inexistente.
- Intentar eliminar sin operaciones registradas.
- Verificar actualización del estado de la posición después de eliminar una operación.

# Gestión de posiciones

- Crear una posición automáticamente.
- Agregar compras a una posición existente.
- Crear múltiples posiciones para un mismo activo.
- Mostrar posiciones abiertas.
- Mostrar posiciones cerradas.
- Mostrar resumen de una posición.
- Mostrar resumen de un activo.
- Eliminar automáticamente una posición sin operaciones.
- Eliminar automáticamente una posición sin operaciones.
- Cierre automático de una posición cuando la cantidad llega a 0.
- Reapertura automática de una posición cuando vuelve a tener cantidad disponible.
- Mostrar resumen de la cartera. 
- Verificar actualización de la posición después de una compra contextual.
- Verificar actualización de la posición después de una venta contextual.

# Dashboard

- Mostrar capital invertido.
- Mostrar ganancia realizada.
- Mostrar cantidad total de posiciones.
- Mostrar cantidad de posiciones abiertas.
- Mostrar liquidez.
- Mostrar resumen por activo.
- Mostrar histórico por activo.
- Mostrar posiciones abiertas.
- Acceder al detalle de una posición.
- Registrar una compra directamente desde una posición abierta.
- Registrar una venta directamente desde una posición abierta.
- Utilizar Max desde una posición abierta.
- Verificar que las acciones contextuales correspondan a la posición seleccionada.
- Verificar que una operación contextual exitosa vuelva al Dashboard.
- Verificar que una operación contextual con error vuelva al Dashboard mostrando el mensaje correspondiente.

# Navegación y menús

- Seleccionar IDs inexistentes.
- Volver al menú desde cada opción. 
- Ingresar opciones inválidas.
- Menús sin datos disponibles.
- Acceder al flujo independiente de compra desde el menú principal.
- Acceder al flujo independiente de venta desde el menú principal.
- Acceder al detalle de una posición desde el Dashboard.

# Persistencia

- Registrar una compra y reiniciar la aplicación.
- Registrar una venta y reiniciar la aplicación.
- Verificar que las posiciones mantengan su estado después de reiniciar.
- Verificar que las operaciones mantengan sus datos después de reiniciar.
- Verificar que la configuración mantenga el capital inicial.
- Verificar que la configuración mantenga el ajuste de liquidez.
- Verificar que la liquidez calculada se mantenga correctamente después de reiniciar.