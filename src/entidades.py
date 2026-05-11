from abc import ABC, abstractmethod
# Define la jerarquía de errores personalizados del sistema Software FJ

class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad
# Permite una gestión de errores controlada.
    @abstractmethod
    def __str__(self):
        pass
