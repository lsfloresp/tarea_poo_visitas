from visitas_app.modelos.visitante import Visitante

class VisitaServicio:
    def __init__(self):
        self.__visitantes = []  # encapsulado

    def registrar(self, cedula, nombre, motivo):
        if self.buscar_por_cedula(cedula):
            return False
        visitante = Visitante(cedula, nombre, motivo)
        self.__visitantes.append(visitante)
        return True

    def listar(self):
        return self.__visitantes

    def eliminar(self, cedula):
        visitante = self.buscar_por_cedula(cedula)
        if visitante:
            self.__visitantes.remove(visitante)
            return True
        return False

    def buscar_por_cedula(self, cedula):
        for v in self.__visitantes:
            if v.cedula == cedula:
                return v
        return None