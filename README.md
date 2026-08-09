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

Desarrollar una plataforma web para la gestión y análisis de una cartera de inversiones personales.

La aplicación busca ofrecer una visión completa de la cartera mediante indicadores, resúmenes por activo, seguimiento de posiciones y operaciones históricas, permitiendo registrar compras y ventas de activos financieros desde una interfaz web intuitiva.

El proyecto tiene como objetivo principal aplicar buenas prácticas de desarrollo de software mientras evoluciona desde una aplicación de consola hacia una aplicación web completa.

---

## ⭐ Características principales

- Arquitectura modular.
- Aplicación web desarrollada con Flask.
- Persistencia automática en JSON.
- Gestión de múltiples posiciones por activo.
- Dashboard con métricas generales.
- Configuración del capital inicial.
- Cálculos financieros automáticos.
- Preparado para migrar a SQLite.

---

## 🚀 Estado actual del proyecto

🚧 En desarrollo activo.

El sistema cuenta actualmente con un núcleo funcional desarrollado en Python, organizado mediante una arquitectura modular basada en separación de responsabilidades.

Entre las funcionalidades implementadas se encuentran:

- Registro de compras.
- Registro de ventas.
- Creación automática de posiciones.
- Gestión de posiciones abiertas y cerradas.
- Dashboard con indicadores generales.
- Configuración del capital inicial.
- Cálculo de liquidez.
- Cálculo de capital invertido.
- Cálculo de precio promedio.
- Cálculo de Ganancia realizada.
- Resumen por posición.
- Resumen consolidado por activo.
- Visualización de todas las operaciones.
- Persistencia automática en JSON.

---

## 🏗️ Arquitectura actual

### Flujo general de la aplicación

```
                 Usuario
                    |
                    ↓
                main.py
                    |
                    ↓
                menu.py
                    |
                    ↓
              servicios.py
          /        |        \
         ↓         ↓         ↓
validaciones   operaciones  persistencia
                      |
                      ↓
                archivos JSON
          (operaciones.json / posiciones.json)
                    ↓
              calculos.py
                    |
                    ↓
           visualizacion.py
```

### Responsabilidad de los módulos

El proyecto está dividido por responsabilidades:

- menu.py → interacción con el usuario.
- servicios.py → reglas de negocio.
- validaciones.py → validaciones.
- operaciones.py → gestión de operaciones.
- posiciones.py → gestión de posiciones.
- calculos.py → cálculos financieros.
- visualizacion.py → salida por consola.
- persistencia.py → Almacenamiento.
- utilidades.py → funciones auxiliares.

Esta separación facilita el mantenimiento del proyecto y prepara la lógica para futuras integraciones con Flask y una base de datos.

---

## 🛠️ Tecnologías utilizadas 

- Python
- Flask
- HTML
- Jinja2
- JSON
- Git
- GitHub

## 🚀 Tecnologías planificadas

- CSS
- JavaScript
- SQLite
- APIs financieras

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

### Dashboard

- [ ] Tarjetas históricas por activo.
- [ ] Resumen por activo.
- [ ] Valor actual de la cartera.
- [ ] Rentabilidad por activo.
- [ ] Ganancias no realizadas.

### Gestión

- [ ] Editar operaciones.
- [ ] Eliminar operaciones.
- [ ] Historial de posiciones cerradas.
- [ ] Historial completo de operaciones.

### Persistencia

- [ ] Migración de JSON a SQLite.

### Integraciones

- [ ] Obtener precios mediante APIs.
- [ ] Actualización automática del valor de mercado.

### Interfaz

- [ ] Mejorar el diseño responsive.
- [ ] Incorporar gráficos y visualizaciones.

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