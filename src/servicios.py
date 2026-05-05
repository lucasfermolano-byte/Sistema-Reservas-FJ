from servicio import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.precio_base * horas

    def descripcion(self):
        return "Reserva de sala por horas"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias):
        return self.precio_base * dias

    def descripcion(self):
        return "Alquiler de equipos por días"


class Asesoria(Servicio):

    def calcular_costo(self, horas, descuento=0):
        total = self.precio_base * horas
        return total - (total * descuento)

    def descripcion(self):
        return "Asesoría especializada"
