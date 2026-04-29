from excepciones import ReservaError
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ReservaError("Cliente no válido")

        if servicio is None:
            raise ReservaError("Servicio no válido")

        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def calcular_total(self):
        return self.servicio.calcular_costo(self.duracion)

    def mostrar_info(self):
        return f"Cliente: {self.cliente.get_nombre()} | Estado: {self.estado}"
