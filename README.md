# todolist-RSanchez

# Descripción
Aplicación para gestionar tareas personales, usando programación procedural, orientada a objetos y funcional.

# Instrucciones de ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/RodrigoSanchezB/todolist-RSanchez.git
cd todolist-RSanchez

# ToDo List - Rodrigo Sánchez

Aplicación de consola en Python para gestionar tareas personales.

## ✅ Funcionalidades

- Crear, editar y eliminar tareas.
- Asignar categorías a tareas.
- Filtrar tareas por estado (pendiente, en progreso, completada).
- Ver métricas como:
  - Porcentaje de tareas completadas.
  - Promedio de duración de las tareas.

## 💻 Tecnologías y paradigmas utilizados

- Lenguaje: Python 3
- Paradigma Procedural: Menús, validaciones, persistencia en archivos.
- Paradigma Orientado a Objetos: Clases `Tarea` y `Categoria`.
- Paradigma Funcional: Uso de `filter`, `map`, `reduce`, `lambda` para estadísticas.

## 📁 Estructura del proyecto

todolist-RSanchez/
│
├── main.py
├── README.md
├── requirements.txt
├── data/
│ ├── tareas.json
│ └── categorias.json
├── docs/
│ └── diseño.md
├── models/
│ ├── tarea.py
│ └── categoria.py
└── src/
├── menu.py
├── gestor_tareas.py
└── estadisticas.py

## ▶️ Instrucciones para ejecutar

```bash
python main.py
