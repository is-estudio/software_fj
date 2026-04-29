from excepciones import ClienteInvalidoError

class Cliente:
    def __init__(self, nombre, email):
        if not nombre:
            raise ClienteInvalidoError("Nombre vacío")

        if "@" not in email:
            raise ClienteInvalidoError("Correo inválido")

        self.__nombre = nombre
        self.__email = email

    def get_nombre(self):
        return self.__nombre
