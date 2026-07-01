# 📊 Cartera de Activos

Sistema en desarrollo para el registro, análisis y gestión de una cartera de inversiones.

El proyecto implementa actualmente la **lógica central en Python** organizada por capas y módulos, permitiendo registrar operaciones financieras, calcular métricas de la cartera, y preparar la aplicación para su futura evolucion hacia una aplicación web full-stack con Flask.

---

## 🚀 Estado actual del proyecto

El sistema ya cuenta con una base funcional en Python que permite:

- Registrar compras y ventas de activos.
- Validar operaciones antes de ser registradas.
- Controlar que no sea posible vender una cantidad superior a la disponible.
- Normalizar los datos ingresados por el usuario.
- Calcular automáticamente la cantidad adquirida según el monto invertido y el precio de compra.
- Calcular capital histórico invertido.
- Calcular cantidad actual de cada activo.
- Calcular precio promedio de compra.
- Calcular capital recuperado mediante ventas.
- Calcular ganancia realizada.
- Generación de un resumen completo por activo.
- Generación de un resumen total de cartera.

---



🏗️ Arquitectura actual

El proyecto se encuentra dividido en módulos con responsabilidades específicas:

```
main.py ──> servicios.py ──> operaciones.py / calculos.py
                             └─ (Responsabilidad de cada módulo)
```

Responsabilidad de cada módulo

main.py

- Punto de entrada del programa.
- Simula la interacción del usuario.
- Invoca la capa de servicios.

servicios.py

- Centraliza las reglas de negocio.
- Valida compras y ventas.
- Coordina el flujo de cada operación.

operaciones.py

- Registra las operaciones.
- Obtiene operaciones y activos registrados.

calculos.py

- Analiza cada activo.
- Calcula métricas financieras.
- Genera resúmenes de la cartera.

Esta separación facilita el mantenimiento del proyecto y prepara la lógica para futuras integraciones con Flask y una base de datos.

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
]
```
---

## 🎯 Objetivo

Construir una plataforma web que permita:

* Registrar compras y ventas de activos.
* Gestionar una cartera de inversiones en tiempo real.
* Visualizar rendimiento y métricas clave.
* Consultar rendimiento histórico.
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

### Backend

* JSON (próxima etapa de persistencia)
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

Actualmente el proyecto cuenta con:

✅ Arquitectura modular.
✅ Separación entre lógica de negocio, cálculos y operaciones.
✅ Validaciones para compras y ventas.
✅ Control de disponibilidad antes de vender un activo.
✅ Cálculo de métricas financieras.
✅ Resúmenes por activo y cartera.

La siguiente etapa consistirá en incorporar persistencia utilizando archivos JSON antes de migrar posteriormente a una base de datos.

---

## 🧩 Próximos pasos

* [ ] Incorporar persistencia mediante JSON.
* [ ] Refactorizar funciones reutilizables cuando sea necesario.
* [ ] Crear API con Flask.
* [ ] Conectar base de datos.
* [ ] Desarrollar interfaz web con HTML/CSS/JS.
* [ ] Crear un dashboard para visualizar la cartera.
* [ ] Agregar cálculo de ganancias no realizadas.
* [ ] Integrar precios de mercado mediante APIs.

---

## 👨‍💻 Autor

Leandro Floridia

Proyecto personal desarrollado como parte de mi proceso de aprendizaje en:

- Programación en Python
- Arquitectura de Software
- Desarrollo web
- Ciencia de datos aplicada a finanzas
- Git y GitHub

El objetivo del proyecto es evolucionar progresivamente desde una aplicación de consola hasta una aplicación web completa, aplicando buenas prácticas de programación y diseño de software durante todo el proceso.
