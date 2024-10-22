from dataclasses import dataclass

@dataclass
class Usuario:
    nombre : str
    id : int
    
    def obtener_nombre (self):
        return self.nombre
    
    def obtener_id (self):
        return self.id

    @staticmethod
    def validar_id(id):
        #Logica para validar id
        pass

    @classmethod
    def contar_usuarios(cls, usuarios):
        return len(usuarios)
        #Logica para contar los ususarios

    #Formato de cadena legible.
    def __str__(self):
        return f"Usuario: {self.nombre}, Id: {self.id}"
    
    #Representación adecuada para depuración.
    def __repr__(self):
        return f"Usuario(nombre:{self.nombre}, Id:{self.id})"


class Lector(Usuario):
    def __init__(self,nombre, id):
        super().__init__(nombre, id)
        self.libros_prestados = []

    #Property para gestionar la lista de libros prestados
    @property
    def libros_prestados(self):
        return self.libros_prestados

    #Metodos de Instancia
    def tomar_libro(self, libro):
        #Agregar a la lista de libros prestados(Lector)
        pass

    def devolver_libro(self, libro):
        #Eliminar de la lista de libros prestados(Lector)
        pass

        #raise Exception(f"El libro '{libro.titulo}' no fue prestado.")