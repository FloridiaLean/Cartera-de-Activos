# 📊 Cartera de Activos

Sistema en desarrollo para el registro, análisis y gestión de una cartera de inversiones.

El proyecto implementa actualmente la **lógica central en Python** para el manejo de operaciones financieras (compras y ventas de activos), y será evolucionado progresivamente hacia una aplicación web full-stack con Flask.

---

## 🚀 Estado actual del proyecto

El sistema ya cuenta con una base funcional en Python que permite:

- Registro de operaciones de compra y venta de activos.
- Control de cantidad de activos en cartera.
- Cálculo de capital invertido por activo.
- Cálculo de precio promedio de compra.
- Registro de capital recuperado por ventas.
- Cálculo de ganancia realizada.
- Generación de un resumen completo por activo.
- Generación de un resumen total de cartera.

---

## 🧠 Ejemplo de salida actual

El sistema genera un resumen estructurado como lista de diccionarios:

```python
[
    {
        'activo': 'BTC',
        'cantidad_actual': 0.0031,
        'capital_invertido': 300,
        'precio_promedio': 64500,
        'capital_recuperado': 140,
        'ganancia_realizada': 11
    },
    {
        'activo': 'ETH',
        'cantidad_actual': 0.14,
        'capital_invertido': 270,
        'precio_promedio': 1450,
        'capital_recuperado': 18,
        'ganancia_realizada': 2
    }
]
```
---

## 🎯 Objetivo

Construir una plataforma web que permita:

* Registrar compras y ventas de activos.
* Gestionar una cartera de inversiones en tiempo real.
* Visualizar rendimiento y métricas clave.
* Integrar datos de mercado.
* Persistir información en una base de datos.
* Ofrecer una interfaz web intuitiva.

---

## 🧠 Funcionalidades actuales (Python)

* Registro de compras de activos.
* Registro de ventas de activos.
* Cálculo de cantidad adquirida según inversión y precio.
* Control de cantidad actual por activo.
* Cálculo de capital invertido.
* Cálculo de precio promedio de compra.
* Consulta de operaciones por activo.

---

## 🛠️ Tecnologías 

Este proyecto evolucionará hacia un app web full-stack:

### Backend

* Python
* Flask (API y servidor web)
* Base de datos (SQLite / PostgreSQL en etapas futuras)

### Frontend

* HTML
* CSS
* JavaScript

### Otros

* Git & GitHub para control de versiones

---

## 📌 Estado actual

🚧 Estado del desarrollo

El proyecto se encuentra en fase inicial pero funcional:

✔ Lógica de operaciones implementada
✔ Sistema de cálculo financiero funcionando
✔ Resúmenes por activo y cartera listos
🚧 Preparado para migración a backend web
* Se irán agregando capas de frontend, backend y base de datos progresivamente.

---

## 🧩 Próximos pasos

* [ ] Separar el código en módulos.
* [ ] Crear API con Flask.
* [ ] Conectar base de datos para persistencia.
* [ ] Desarrollar interfaz web con HTML/CSS/JS.
* [ ] Mostrar cartera en un dashboard.
* [ ] Agregar cálculo de ganancias realizadas y no realizadas.
* [ ] Integrar precios de mercado.

---

## 👨‍💻 Autor

Leandro Floridia
Programación en Python
Desarrollo web
Ciencia de datos aplicada a finanzas
Proyecto personal en desarrollo como parte de mi aprendizaje en programación, desarrollo web y ciencia de datos.
