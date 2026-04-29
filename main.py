from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_error

# CASOS DE PRUEBA

def ejecutar_pruebas():

    # 1. Cliente válido
    try:
        c1 = Cliente("Maria", "maria@email.com")
    except Exception as e:
        registrar_error(str(e))

    # 2. Cliente inválido
    try:
        c2 = Cliente("", "correo")
    except Exception as e:
        registrar_error(str(e))

    # 3. Servicio
    sala = ReservaSala("Sala", 50)

    # 4. Reserva válida
    try:
        r1 = Reserva(c1, sala, 2)
        print("Total:", r1.calcular_total())
        r1.confirmar()
    except Exception as e:
        registrar_error(str(e))

    # 5. Reserva inválida
    try:
        r2 = Reserva(c1, sala, -1)
    except Exception as e:
        registrar_error(str(e))

    # 6–10 más casos
    try:
        equipo = AlquilerEquipo("Equipo", 30)
        asesoria = Asesoria("Asesoria", 100)

        r3 = Reserva(c1, equipo, 3)
        print(r3.calcular_total())

        r4 = Reserva(c1, asesoria, 1)
        print(r4.calcular_total())

    except Exception as e:
        registrar_error(str(e))

    finally:
        print("Ejecución finalizada sin detener el sistema")


if __name__ == "__main__":
    ejecutar_pruebas()
