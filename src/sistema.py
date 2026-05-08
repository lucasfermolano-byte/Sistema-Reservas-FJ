from logger import Logger
from reserva import Reserva

class Sistema:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        try:
            self.clientes.append(cliente)
            Logger.log(f"Cliente agregado: {cliente}")
        except Exception as e:
            Logger.log(f"Error al agregar cliente: {e}")

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def crear_reserva(self, cliente, servicio, duracion):
        try:
            reserva = Reserva(cliente, servicio, duracion)
            costo = reserva.procesar()
            self.reservas.append(reserva)
            Logger.log(f"Reserva exitosa - Costo: {costo}")
        except Exception as e:
            Logger.log(f"Error en reserva: {e}")# clase sistema
