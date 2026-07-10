# 📊 Cartera de Activos

Aplicación en desarrollo para la gestión y análisis de una cartera de inversiones, desarrollada con Python y una arquitectura modular, diseñada para evolucionar hacia una aplicación web completa utilizando Flask.

El foco del proyecto no es únicamente el resultado final, sino también el aprendizaje progresivo de conceptos como:

- Programación orientada a funciones.
- Modularización.
- Separación de responsabilidades.
- Persistencia de datos.
- Validaciones.
- Arquitectura escalable.
- Control de versiones con Git.

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

## ⭐ Características principales

- Arquitectura modular.
- Persistencia automática en JSON.
- Gestión de múltiples posiciones por activo.
- Cálculos financieros automáticos.
- Menú interactivo en consola.
- Preparado para migrar a Flask y SQLite.

---

## 🚀 Estado actual del proyecto

🚧 En desarrollo activo.

El sistema cuenta actualmente con un núcleo funcional desarrollado en Python, organizado mediante una arquitectura modular basada en separación de responsabilidades.

Entre las funcionalidades implementadas se encuentran:

- Registro de compras.
- Registro de ventas.
- Creación automática de posiciones.
- Posibilidad de agregar compras a posiciones existentes.
- Posibilidad de crear múltiples posiciones para un mismo activo.
- Cálculo automático de cantidad comprada.
- Cálculo de precio promedio.
- Capital histórico.
- Capital recuperado.
- Ganancia realizada.
- Estado de la posición (Abierta / Cerrada).
- Resumen individual por posición.
- Resumen consolidado por activo.
- Visualización de todas las operaciones.
- Persistencia automática en JSON.

---

## 🏗️ Arquitectura actual

### Flujo general de la aplicación

```
main.py
    │
    ▼
menu.py  ◄───────────────────────────────────────────┐
    │                                                │
    ▼                                                │
servicios.py                                         │
    │                                                │
    ├──────────────┐──────────────┐                  │
    ▼              ▼              ▼                  │
validaciones.py   operaciones.py  persistencia.py    │
    │              │                                 │
    ▼              ▼                                 │
utilidades.py    posiciones.py                       │
    │                                                │
    ▼                                                │
calculos.py                                          │
    │                                                │ 
    ▼                                                │
visualizacion.py  ───────────────────────────────────┘
```

### Responsabilidad de los módulos

El proyecto está dividido por responsabilidades:

- menu.py → interacción con el usuario.
- servicios.py → lógica de negocio.
- operaciones.py → registro de operaciones.
- posiciones.py → gestión de posiciones.
- calculos.py → cálculos financieros.
- visualizacion.py → impresión de información.
- persistencia.py → lectura y escritura en JSON.
- validaciones.py → validaciones de datos.
- utilidades.py → funciones auxiliares.

Esta separación facilita el mantenimiento del proyecto y prepara la lógica para futuras integraciones con Flask y una base de datos.

---

## 🛠️ Tecnologías utilizadas 

- Python
- JSON
- Git
- GitHub

## 🚀 Tecnologías planificadas

- Flask
- HTML
- CSS
- JavaScript
- SQLite

---

## 🧠 Ejemplo de salida actual

El sistema genera un resumen detallado de cada posición registrada en la cartera:

## Salida de consola:

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
Capital histórico: $250.00
Capital recuperado: $0.00
=================================================
Cantidad total: 0.00341498 BTC
Cantidad actual: 0.00341498 BTC
=================================================
Precio promedio: $73,206.82
Ganancia realizada: $0.00
=================================================
```

## Estructura interna de los datos

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

## 📚 Conceptos aplicados

Durante el desarrollo de este proyecto se aplican conceptos como:

- Separación de responsabilidades.
- Programación modular.
- Validación de datos.
- Persistencia de información.
- Arquitectura escalable.
- Refactorización continua.
- Control de versiones con Git.

---

## 🧩 Próximos pasos

* [ ] Editar operaciones.
* [ ] Eliminar operaciones.
* [ ] Cierre automático de posiciones.
* [ ] Migración de JSON a SQLite.
* [ ] Desarrollar una interfaz web con Flask.   
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

---