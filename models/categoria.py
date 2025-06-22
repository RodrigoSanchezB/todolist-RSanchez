class Categoria:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Categoria(**data)
