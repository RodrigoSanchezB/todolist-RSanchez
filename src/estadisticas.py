from functools import reduce
from datetime import datetime

def calcular_porcentaje_completadas(tareas):
    if not tareas:
        return 0
    completadas = list(filter(lambda t: t.estado == "completada", tareas))
    return round(len(completadas) / len(tareas) * 100, 2)

def calcular_promedio_duracion(tareas):
    # Solo tareas completadas con fecha_inicio y fecha_fin definidas y válidas
    tareas_validas = list(filter(lambda t: t.estado == "completada" and t.fecha_inicio and t.fecha_fin, tareas))
    if not tareas_validas:
        return 0
    duraciones = list(map(lambda t: calcular_dias(t.fecha_inicio, t.fecha_fin), tareas_validas))
    total = reduce(lambda acc, x: acc + x, duraciones, 0)
    return round(total / len(duraciones), 2)

def calcular_dias(fecha_inicio, fecha_fin):
    try:
        ini = datetime.fromisoformat(fecha_inicio)
        fin = datetime.fromisoformat(fecha_fin)
        return max((fin - ini).days, 1)  # mínimo 1 día
    except Exception:
        return 0

def mostrar_estadisticas(tareas):
    print("\n--- Estadísticas ---")
    print(f"Porcentaje completadas: {calcular_porcentaje_completadas(tareas)}%")
    print(f"Promedio de duración (días): {calcular_promedio_duracion(tareas)}")
