import json
from models.tarea import Tarea
from models.categoria import Categoria

RUTA_TAREAS = "data/tareas.json"
RUTA_CATEGORIAS = "data/categorias.json"

def cargar_tareas():
    try:
        with open(RUTA_TAREAS, "r") as f:
            return [Tarea.from_dict(t) for t in json.load(f)]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(RUTA_TAREAS, "w") as f:
        json.dump([t.to_dict() for t in tareas], f, indent=2)

def cargar_categorias():
    try:
        with open(RUTA_CATEGORIAS, "r") as f:
            return [Categoria.from_dict(c) for c in json.load(f)]
    except FileNotFoundError:
        return []

def guardar_categorias(categorias):
    with open(RUTA_CATEGORIAS, "w") as f:
        json.dump([c.to_dict() for c in categorias], f, indent=2)

def generar_id(lista):
    return max((item.id for item in lista), default=0) + 1
