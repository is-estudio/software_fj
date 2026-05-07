from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, horas):

        if horas <= 0:
            raise ReservaError(
                "La duración debe ser positiva"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        try:

            costo = self.servicio.calcular_costo(
                self.horas
            )

            self.confirmar()

            return costo

        except Exception as e:

            raise ReservaError(
                "Error al procesar reserva"
            ) from e
