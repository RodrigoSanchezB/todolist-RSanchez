from datetime import datetime

class Tarea:
    def __init__(self, id, titulo, descripcion, categoria, estado="pendiente", fecha_inicio=None, fecha_fin=None):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.categoria = categoria
        self.estado = estado
        self.fecha_inicio = fecha_inicio or datetime.now().isoformat()
        self.fecha_fin = fecha_fin

    def marcar_completada(self):
        self.estado = "completada"
        self.fecha_fin = datetime.now().isoformat()

    def actualizar(self, titulo=None, descripcion=None, categoria=None, estado=None):
        if titulo:
            self.titulo = titulo
        if descripcion:
            self.descripcion = descripcion
        if categoria:
            self.categoria = categoria
        if estado:
            self.estado = estado

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Tarea(**data)
