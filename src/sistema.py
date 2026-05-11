from logger import Logger
from reserva import Reserva

class Sistema:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        try:
            # Validación de duplicados (Requisito de estabilidad)
            if any(c.id == cliente.id for c in self.clientes):
                raise Exception(f"El ID {cliente.id} ya está registrado.")
            self.clientes.append(cliente)
        
        except Exception as e:
            # Manejo del error
            Logger.log(f"Error al agregar cliente: {e}")
            print(f"Error: {e}")
            
        else:
            #Se ejecuta solo si todo salió bien
            Logger.log(f"Éxito: Cliente {cliente.id} guardado correctamente.")
            
        finally:
        
            print(f"Intento de registro finalizado para el ID: {cliente.id}")
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
