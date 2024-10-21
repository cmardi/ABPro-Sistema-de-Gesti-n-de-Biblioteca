from dataclasses import dataclass

@dataclass
class Usuario:
    nombre : str
    id : int
    
    
    @staticmethod
    def validar_id(id):
        pass

    @classmethod
    def contar_usuarios(cls):
        pass

