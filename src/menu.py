# Importaciones necesarias
from src.gestor_tareas import (cargar_tareas, guardar_tareas, cargar_categorias, guardar_categorias, generar_id)
from models.tarea import Tarea
from models.categoria import Categoria
from src.estadisticas import mostrar_estadisticas
from datetime import datetime

# Función principal del menú
def mostrar_menu():
    tareas = cargar_tareas()
    categorias = cargar_categorias()
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear nueva tarea")
        print("2. Editar tarea existente")
        print("3. Eliminar tarea")
        print("4. Listar tareas por estado")
        print("5. Crear nueva categoría")
        print("6. Mostrar estadísticas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_tarea(tareas, categorias)
        elif opcion == "2":
            editar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            listar_tareas_por_estado(tareas)
        elif opcion == "5":
            crear_categoria(categorias)
        elif opcion == "6":
            mostrar_estadisticas(tareas)
        elif opcion == "0":
            guardar_tareas(tareas)
            guardar_categorias(categorias)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

# Función para crear tareas con fecha de inicio
def crear_tarea(tareas, categorias):
    if not categorias:
        print("No hay categorías disponibles. Se creará una categoría genérica 'General'.")
        categoria_generica = Categoria(id=1, nombre="General")
        categorias.append(categoria_generica)

    titulo = input("Título: ")
    descripcion = input("Descripción: ")

    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD) o dejar vacío para hoy: ").strip()
    if not fecha_inicio:
        fecha_inicio = datetime.now().date().isoformat()

    fecha_fin = input("Fecha de fin (YYYY-MM-DD) o dejar vacío si aún no se ha completado: ").strip()
    if fecha_fin == "":
        fecha_fin = None

    print("Categorías disponibles:")
    for c in categorias:
        print(f"{c.id} - {c.nombre}")
    try:
        id_categoria = int(input("ID de categoría: "))
        categoria = next((c.nombre for c in categorias if c.id == id_categoria), "General")
    except ValueError:
        categoria = "General"

    nueva_tarea = Tarea(
        id=generar_id(tareas),
        titulo=titulo,
        descripcion=descripcion,
        categoria=categoria,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin
    )
    tareas.append(nueva_tarea)
    print("Tarea creada.")
    
# Editar tarea con asignación de fecha de fin
def editar_tarea(tareas):
    listar_tareas(tareas)
    id_tarea = int(input("ID de la tarea a editar: "))
    tarea = next((t for t in tareas if t.id == id_tarea), None)
    if tarea:
        nuevo_titulo = input(f"Nuevo título ({tarea.titulo}): ") or tarea.titulo
        nueva_desc = input(f"Nueva descripción ({tarea.descripcion}): ") or tarea.descripcion
        nuevo_estado = input(f"Nuevo estado (pendiente/en progreso/completada): ") or tarea.estado
        tarea.actualizar(nuevo_titulo, nueva_desc, None, nuevo_estado)
        if nuevo_estado == "completada" and not tarea.fecha_fin:
            tarea.fecha_fin = datetime.now().date().isoformat()
        print("Tarea actualizada.")
    else:
        print("Tarea no encontrada.")

# Eliminar tarea
def eliminar_tarea(tareas):
    listar_tareas(tareas)
    id_tarea = int(input("ID de la tarea a eliminar: "))
    tareas[:] = [t for t in tareas if t.id != id_tarea]
    print("Tarea eliminada.")

# Filtrar tareas por estado
def listar_tareas_por_estado(tareas):
    estado = input("Ingrese el estado (pendiente/en progreso/completada): ").strip()
    filtradas = list(filter(lambda t: t.estado == estado, tareas))
    if filtradas:
        for t in filtradas:
            print(f"[{t.id}] {t.titulo} ({t.estado}) - {t.categoria}")
    else:
        print("No hay tareas con ese estado.")

# Crear categoría
def crear_categoria(categorias):
    nombre = input("Nombre de nueva categoría: ")
    nueva = Categoria(id=generar_id(categorias), nombre=nombre)
    categorias.append(nueva)
    print("Categoría creada.")

# Mostrar tareas con duración (si están completadas)
def listar_tareas(tareas):
    for t in tareas:
        if t.estado == "completada" and t.fecha_inicio and t.fecha_fin:
            duracion = (datetime.fromisoformat(t.fecha_fin) - datetime.fromisoformat(t.fecha_inicio)).days
            print(f"[{t.id}] {t.titulo} - {t.estado} ({t.categoria}) | Duración: {duracion} días")
        else:
            print(f"[{t.id}] {t.titulo} - {t.estado} ({t.categoria})")
