from enum import Enum

class Roles(Enum):
    ADMINISTRADOR = (1, 'Administrador')
    SUPERVISOR = (2, 'Supervisor')
    AGENTE = (3, 'Agente')

    def __init__(self, value, label):
        self._value_ = value
        self.label = label
