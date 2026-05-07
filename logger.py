from datetime import datetime

class Logger:

    @staticmethod
    def registrar(mensaje):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"[{datetime.now()}] {mensaje}\n")

