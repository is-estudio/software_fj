from abc import ABC
from excepciones import ClienteError


class Persona(ABC):

    def __init__(self, nombre):
        self.nombre = nombre


class Cliente(Persona):

    def __init__(self, nombre, correo, telefono):

        super().__init__(nombre)

        self.__correo = None
        self.__telefono = None

        self.correo = correo
        self.telefono = telefono

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if "@" not in valor:
            raise ClienteError("Correo inválido")

        self.__correo = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not valor.isdigit():
            raise ClienteError("Teléfono inválido")

        self.__telefono = valor

    def mostrar(self):

        return (
            f"{self.nombre} - "
            f"{self.__correo} - "
            f"{self.__telefono}"
        )