from abc import ABC, abstractmethod

# CLASE ABSTRACTA "isabel"
class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# CLASE 1: Reserva de Sala "isabel"
class ReservaSala(Servicio):
    def calcular_costo(self, duracion):
        return self.precio_base * duracion

    def descripcion(self):
        return f"Reserva de sala por {self.precio_base} por hora"


# CLASE 2: Alquiler de Equipos "isabel"
class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion):
        return (self.precio_base * duracion) + 20

    def descripcion(self):
        return "Alquiler de equipos con costo adicional"


# CLASE 3: Asesoría "isabel"
class Asesoria(Servicio):
    def calcular_costo(self, duracion):
        return self.precio_base * duracion * 1.2

    def descripcion(self):
        return "Asesoría especializada"
