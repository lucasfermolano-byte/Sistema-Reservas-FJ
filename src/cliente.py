from excepciones import ClienteInvalidoError

class Cliente:

    def __init__(self, id, nombre, email):
        self.id = id
        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        if not nombre:
            raise ClienteInvalidoError("El nombre no puede estar vacío")
        self._nombre = nombre

    def set_email(self, email):
        if "@" not in email:
            raise ClienteInvalidoError("Email inválido")
        self._email = email

    def __str__(self):
        return f"{self._nombre} - {self._email}"
