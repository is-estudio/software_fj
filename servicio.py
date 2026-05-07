from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas, impuesto=0.19):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        subtotal = horas * self.tarifa

        return subtotal + (subtotal * impuesto)

    def descripcion(self):

        return "Reserva de salas empresariales"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas, descuento=0):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        subtotal = horas * self.tarifa

        return subtotal - descuento

    def descripcion(self):

        return "Alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        return horas * self.tarifa * 1.2

    def descripcion(self):

        return "Asesorías especializadas"