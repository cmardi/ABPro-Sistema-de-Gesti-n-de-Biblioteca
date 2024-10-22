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

#@property

class Adminsitrador(Usuario):

    @staticmethod
    def agregar_libro():
        #Logica para agregar Libro
        pass

    @staticmethod
    def eliminar_libro():
        #Logica para agregar Libro
        pass

    @classmethod
    def conteo_libros_disponiles(cls):
        pass

class LectorAdminsitrador(Lector, Adminsitrador):
    #Hereda las capacidades de las clases Lector/Adminsitrador
    pass

@dataclass
class Libro():
    titulo : str
    autor : str
    codigounico : int
    estado: str = "disponible"

    def estado_libro():
        pass

    def contar_libros():
        pass

    #FALTAN LAS PROPIEDADES
    """
    Utilizar propiedades para acceder y modificar el estado de un libro de
    manera controlada (por ejemplo, para cambiar el estado de "disponible" a
    "prestado").

    """
    #Metodos Dunder de Libro
    def __str__(self):
        return f"{self.titulo} por {self.autor}, Estado: {self.estado}"

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, codigo={self.codigo}, estado={self.estado})"
    

class Prestamo():
    pass


class LibroNoDisponibleError(Exception):
    pass

class LibroNoEncontradoError(Exception):
    pass