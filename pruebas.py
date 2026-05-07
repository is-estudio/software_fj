from software_fj.cliente import Cliente
from software_fj.servicio import *
from software_fj.reserva import Reserva
from software_fj.logger import Logger

operaciones = []

try:
    c1 = Cliente("Juan", "juan@gmail.com", "123456")
    operaciones.append(c1)

    c2 = Cliente("Ana", "correo_invalido", "abc")
    operaciones.append(c2)

except Exception as e:
    Logger.registrar(e)

try:
    s1 = ReservaSala("Sala VIP", 100)

    r1 = Reserva(c1, s1, 5)

    print(r1.procesar())

except Exception as e:
    Logger.registrar(e)