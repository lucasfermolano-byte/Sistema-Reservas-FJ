# Clase encargada de la persistencia de datos en archivos de texto.
from datetime import datetime
# Registra eventos y fallos en logs/logs.txt para auditoría del tutor.
class Logger:

    @staticmethod
    def log(mensaje):
        with open("logs/logs.txt", "a") as archivo:
            archivo.write(f"{datetime.now()} - {mensaje}\n")
