from dataclasses import dataclass

@dataclass
class Usuario:
    nombre : str
    id_usuario : int
    total_usuarios: int = 0
    
    def __post_init__(self):
        Usuario.total_usuarios += 1     # Incrementa el total de usuarios al crear una instanci
    
    def obtener_nombre (self):
        return self.nombre
    
    def obtener_id (self):
        return self.id_usuario

    @staticmethod
    def validar_id(id_usuario):
        return isinstance(id_usuario, int) and id_usuario > 0   #Validación de id
    
    @classmethod
    def contar_usuarios(cls, usuarios):
        return len(usuarios)    #Lógica para contar los ususarios
        
    def __str__(self):      #Formato de cadena legible.
        return f"Usuario: {self.nombre}, Id: {self.id_usuario}" 
    
    def __repr__(self):     #Representación adecuada para depuración.
        return f"Usuario(nombre:{self.nombre}, Id:{self.id_usuario})"


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