from datetime import datetime

class Logger:

    @staticmethod
    def log(mensaje):
        with open("logs/logs.txt", "a") as archivo:
            archivo.write(f"{datetime.now()} - {mensaje}\n")
