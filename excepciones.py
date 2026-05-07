class ErrorSistema(Exception):
    """Clase base para excepciones del sistema"""
    pass


class ClienteError(ErrorSistema):
    pass


class ServicioError(ErrorSistema):
    pass


class ReservaError(ErrorSistema):
    pass