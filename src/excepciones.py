class ErrorSistema(Exception):
    """Clase base para errores del sistema"""
    pass

class ClienteInvalidoError(ErrorSistema):
    pass

class ServicioNoDisponibleError(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    pass
