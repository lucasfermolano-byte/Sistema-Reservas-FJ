# Archivo: cliente.py
from excepciones import ClienteInvalidoError
from entidades import EntidadBase  # Importamos la base que creamos arriba

class Cliente(EntidadBase): # Heredamos de EntidadBase

    def __init__(self, id, nombre, email):
        # super().__init__ envía el ID a la clase EntidadBase
        super().__init__(id) 
        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        # Validación más robusta para la Fase 4
        if not nombre or len(nombre) < 3:
            raise ClienteInvalidoError("El nombre debe tener al menos 3 caracteres")
        self._nombre = nombre

    def set_email(self, email):
        # Validación estricta de formato
        if "@" not in email or "." not in email:
            raise ClienteInvalidoError("Formato de email inválido (falta @ o punto)")
        self._email = email

    def __str__(self):
        # Implementamos el método obligatorio que pide la base
        return f"CLIENTE [ID: {self.id_entidad}] - Nombre: {self._nombre} - Email: {self._email}"