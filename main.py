from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import registrar_error

def ejecutar_pruebas():

    # 1. Cliente válido
    try:
        c1 = Cliente("Maria", "maria@email.com")
        print("Cliente creado")
    except Exception as e:
        registrar_error(str(e))

    # 2. Cliente inválido
    try:
        c2 = Cliente("", "correo")
    except Exception as e:
        registrar_error(str(e))

    # 3. Servicios
    sala = ReservaSala("Sala", 50)
    equipo = AlquilerEquipo("Equipo", 30)
    asesoria = Asesoria("Asesoria", 100)

    # 4. Reserva válida
    try:
        r1 = Reserva(c1, sala, 2)
        print("Total sala:", r1.calcular_total())
        r1.confirmar()
    except Exception as e:
        registrar_error(str(e))

    # 5. Reserva con error (duración)
    try:
        r2 = Reserva(c1, sala, -1)
    except Exception as e:
        registrar_error(str(e))

    # 6. Reserva con equipo
    try:
        r3 = Reserva(c1, equipo, 3)
        print("Total equipo:", r3.calcular_total())
    except Exception as e:
        registrar_error(str(e))

    # 7. Reserva con asesoría
    try:
        r4 = Reserva(c1, asesoria, 1)
        print("Total asesoría:", r4.calcular_total())
    except Exception as e:
        registrar_error(str(e))

    # 8. Cliente None
    try:
        r5 = Reserva(None, sala, 2)
    except Exception as e:
        registrar_error(str(e))

    # 9. Servicio None
    try:
        r6 = Reserva(c1, None, 2)
    except Exception as e:
        registrar_error(str(e))

    # 10. Otro caso
    try:
        r7 = Reserva(c1, sala, 5)
        print("Total:", r7.calcular_total())
    except Exception as e:
        registrar_error(str(e))

    finally:
        print("El sistema sigue funcionando ✅")


if __name__ == "__main__":
    ejecutar_pruebas()
