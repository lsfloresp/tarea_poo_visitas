from dataclasses import dataclass

@dataclass
class Visitante:
    cedula: str
    nombre: str
    motivo: str

vista servicio
from visitas_app.modelos.visitante import Visitante