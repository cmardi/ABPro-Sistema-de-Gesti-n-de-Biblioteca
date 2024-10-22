from dataclasses import dataclass, field
import csv

@dataclass
class Usuario:
    nombre : str
    id : int
    total_usuarios: int = field(default_factory=list, init=False)
    
    def __post_init__(self):
        Usuario.total_usuarios.append(self)     # Incrementa el total de usuarios al crear una instanci
    
    def obtener_nombre (self):
        return self.nombre
    
    def obtener_id (self):
        return self.id

    @staticmethod
    def validar_id(id_usuario):
        return isinstance(id_usuario, int) and id_usuario > 0   #Validación de id
    
    @classmethod
    def contar_usuarios(cls):
        return len(cls.total_usuarios)    #Lógica para contar los usuarios
    
    @classmethod
    def cargar_usuarios_csv(cls, archivo):
        with open(archivo, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)    # Saltar la cabecera
            for row in reader:
                if row :        # Asegurarse de que la fila no esté vacía
                    id_usuario = int(row[0])
                    nombre_usuario = row[1]
                    if not any(u.id == id_usuario for u in cls.total_usuarios): # Verificar si el usuario ya existe antes de crear una nueva instancia
                        cls(id=id_usuario, nombre=nombre_usuario)   # Crear una instancia
        
    def __str__(self):      #Formato de cadena legible.
        return f"Usuario: {self.nombre}, Id: {self.id}" 
    
    def __repr__(self):     #Representación adecuada para depuración.
        return f"Usuario(nombre:{self.nombre}, id:{self.id})"


class Lector(Usuario):
    def __init__(self,nombre: str, id: int):
        super().__init__(nombre, id)
        self.libros_prestados = []

    #Property para gestionar la lista de libros prestados
    @property
    def libros_prestados(self):
        return self.libros_prestados

    #Metodos de Instancia
    def tomar_libro(self, libro: Libro):
        if libro.estado == 'prestado':
            raise LibroNoDisponibleError(f"El libro {libro.titulo} no está disponible.")
        libro.estado = 'prestado'
        self.libros_prestados.append(libro: Libro)
        
    def devolver_libro(self, libro: Libro):
        if libro not in self.libros_prestados:
            raise ValueError(f"No puedes devolver un libro que no has tomado.")     #Eliminar de la lista de libros prestados(Lector)
        libro.estado = 'disponible'
        self.libros_prestados.remove(libro)
        
    def __str__(self):
        return f"Lector: {self.nombre} (Id: {self.id}"

class Administrador(Usuario):
    @staticmethod
    def agregar_libro(libro: Libro, libros):
        libros.append(libro)    #Logica para agregar Libro
        
    @staticmethod
    def eliminar_libro(id_libro: int, libros):
        libros[:] = [libro for libro in libros if libro.id != id_libro]     #Logica para agregar Libro
        
    @classmethod
    def conteo_libros_disponiles(cls, libros):
        return len(libros)
        
    @staticmethod
    def buscar_libro(id_libro: int, libros):
        for libro in libros:
            if libro.id == id_libro:
                return libro
        raise ValueError(f"Libro con Id {id_libro} no encontrado.")
        
class LectorAdministrador(Lector, Administrador):       #Hereda las capacidades de las clases Lector/Administrador
    
    def __init__(self, nombre: str, id: int):   # Inicializa la clase base Lector
        super().__init__(nombre, id)
    
    def tomar_libro(self, libro):
        self.libros_prestados.append(libro)     # Agrega el libro a su lista de préstamos
    
    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)     # Elimina el libro de su lista de préstamos
    
@dataclass
class Libro:
        id = int
        titulo = str
        autor = str
        _estado: str = field(default='disponible', init = False)
        
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in ['disponible', 'prestado']:
            raise ValueError(f"El estado debe ser 'disponible'  o 'prestado'.")
        self._estado = nuevo_estado
    
    @classmethod    
    def contar_libros(libros):
        return sum(1 for libro in libros if libro.estado == 'disponible')
        
    #Metodos Dunder de Libro
    def __str__(self):
        return f"{self.titulo} por {self.autor}, Estado: {self.estado}"
    def __repr__(self):
        return f"Libro(id={self.id}, titulo={self.titulo} autor={self.autor}, estado={self.estado})"
    
    
class Prestamo():
    pass
class LibroNoDisponibleError(Exception):
    pass
class LibroNoEncontradoError(Exception):
    pass