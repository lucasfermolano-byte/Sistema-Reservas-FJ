from abc import ABC, abstractmethod

class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad

    @abstractmethod
    def __str__(self):
        pass