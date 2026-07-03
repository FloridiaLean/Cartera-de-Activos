# 📊 Cartera de Activos

Sistema en desarrollo para el registro, análisis y gestión de una cartera de inversiones.

El proyecto implementa actualmente la **lógica central en Python** organizada por capas y módulos, permitiendo registrar operaciones financieras, calcular métricas de la cartera, y preparar la aplicación para su futura evolucion hacia una aplicación web full-stack con Flask.

Este proyecto no busca únicamente construir una aplicación de gestión de inversiones. También documenta mi proceso de aprendizaje en desarrollo de software, aplicando progresivamente principios de arquitectura, refactorización y buenas prácticas mientras evoluciona desde una aplicación de consola hacia una aplicación web completa.

---

## 🚀 Estado actual del proyecto

El sistema cuenta actualmente con un núcleo funcional desarrollado en Python, organizado mediante una arquitectura modular basada en separación de responsabilidades.

Entre las funcionalidades implementadas se encuentran:

### Gestión de operaciones
- Registro de compras y ventas de activos.
- Cálculo automático de la cantidad adquirida según el monto invertido y el precio de compra.
- Asociación de operaciones a posiciones de inversión.
- Validación de operaciones antes de ser registradas.

### Gestión de posiciones
- Creación automática de posiciones al realizar la primera compra de un activo.
- Control de posiciones abiertas y cerradas.
- Cierre automático de posiciones cuando la cantidad disponible llega a cero.
- Identificación única de cada posición.

### Validaciones
- Validación de activos ingresados por el usuario.
- Validación de montos, precios y cantidades.
- Control de disponibilidad antes de ejecutar una venta.
- Verificación de consistencia entre activos y posiciones.
- Normalización automática de los datos ingresados.

### Análisis financiero
- Cálculo de capital histórico invertido.
- Cálculo de cantidad total adquirida.
- Cálculo de cantidad actualmente disponible.
- Cálculo de precio promedio de compra.
- Cálculo de capital recuperado mediante ventas.
- Cálculo de ganancia realizada.

### Resúmenes y reportes
- Generación de resúmenes por posición.
- Generación de resúmenes por activo.
- Generación de resúmenes completos de cartera.

---



🏗️ Arquitectura actual

El proyecto se encuentra dividido en módulos con responsabilidades específicas:

```

main.py
    │
    ▼
servicios.py
    │
    ├──────────────┐
    ▼              ▼
validaciones.py   operaciones.py
    │              │
    ▼              ▼
utilidades.py    posiciones.py
          │
          ▼
      calculos.py

```

### Responsabilidad de cada módulo

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

posiciones.py

- Gestiona las posiciones de inversión.
- Crea posiciones.
- Cierra posiciones.
- Consulta posiciones por ID.

validaciones.py

- Centraliza las reglas de validación.
- Valida activos.
- Valida montos.
- Valida precios.
- Valida cantidades.
- Valida posiciones.

utilidades.py

- Normalización de datos.
- Obtención de la fecha actual.
- Funciones reutilizables.

calculos.py

- Analiza cada activo.
- Calcula métricas financieras.
- Genera resúmenes de la cartera.

Esta separación facilita el mantenimiento del proyecto y prepara la lógica para futuras integraciones con Flask y una base de datos.

---
## 🧠 Ejemplo de salida actual

El sistema genera un resumen detallado de cada posición registrada en la cartera:
```
=================================================
Posición #: 1
=================================================
Activo: BTC
Estado: ABIERTA
=================================================
Fecha de apertura: 03/07/2026 13:20
Fecha de cierre: -
=================================================
Capital histórico: 250.0
Capital recuperado: 0.0
=================================================
Cantidad total: 0.0034149825378876775
Cantidad actual: 0.0034149825378876775
=================================================
Precio promedio: 73206.816499459
Ganancia realizada: 0.0
=================================================
```

```
[
    {
        'posicion': 1,
        'activo': 'BTC',
        'estado': 'ABIERTA',
        'fecha_apertura': '03/07/2026 13:20',
        'fecha_cierre': None,
        'capital_historico': 250.0,
        'capital_recuperado': 0.0,
        'cantidad_total': 0.0034,
        'cantidad_actual': 0.0034,
        'precio_promedio': 73206.81,
        'ganancia_realizada': 0.0
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

## 🛠️ Tecnologías 

### Backend

* Python
* JSON (próxima etapa de persistencia)
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

### 🚧 Estado del desarrollo

Actualmente el proyecto cuenta con:

- ✅ Arquitectura modular por responsabilidades.
- ✅ Separación entre lógica de negocio, cálculos y operaciones.
- ✅ Registro de compras y ventas
- ✅ Validaciones centralizadas
- ✅ Normalización de datos.
- ✅ Control de disponibilidad antes de vender un activo.
- ✅ Cálculo de métricas financieras.
- ✅ Resúmenes por posicion, activo y cartera.
- ✅ Refactorización del núcleo para eliminar código duplicado.

La siguiente etapa consistirá en incorporar persistencia utilizando archivos JSON antes de migrar posteriormente a una base de datos.

---

## 🧩 Próximos pasos

* [ ] Incorporar persistencia mediante archivos JSON.
* [ ] Implementar carga automática de la cartera.
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
