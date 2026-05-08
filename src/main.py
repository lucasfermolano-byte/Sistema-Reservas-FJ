from cliente import Cliente
from sistema import Sistema
from servicios import ReservaSala, AlquilerEquipo, Asesoria

sistema = Sistema()

# CLIENTES
try:
    c1 = Cliente(1, "Ana", "ana@email.com")
    sistema.agregar_cliente(c1)

    c2 = Cliente(2, "", "correo")  # error
    sistema.agregar_cliente(c2)
except Exception as e:
    print("Error cliente:", e)

# SERVICIOS
sala = ReservaSala("Sala", 50)
equipo = AlquilerEquipo("Laptop", 30)
asesoria = Asesoria("Consultoría", 100)

sistema.agregar_servicio(sala)
sistema.agregar_servicio(equipo)
sistema.agregar_servicio(asesoria)

# RESERVAS
sistema.crear_reserva(c1, sala, 2)
sistema.crear_reserva(c1, equipo, 3)
sistema.crear_reserva(c1, asesoria, 1)

# ERROR
sistema.crear_reserva(c1, sala, -5)

print("Sistema ejecutado correctamente")
try:
    c3 = Cliente(3, "Carlos", "carlos@email.com")
    sistema.agregar_cliente(c3)

    c4 = Cliente(4, "Laura", "lauraemail.com")  # inválido
    sistema.agregar_cliente(c4)

except Exception as e:
    print("Error cliente:", e)

# Más reservas
sistema.crear_reserva(c3, sala, 4)
sistema.crear_reserva(c3, equipo, 2)
sistema.crear_reserva(c3, asesoria, 5)

# Error de duración
sistema.crear_reserva(c3, sala, 0)

# Otra reserva válida
sistema.crear_reserva(c1, equipo, 1)
