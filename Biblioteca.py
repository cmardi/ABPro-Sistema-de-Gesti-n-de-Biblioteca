from dataclasses import dataclass, field
from datetime import datetime
import csv

class LibroNoDisponibleError(Exception):
    """Excepción lanzada cuando un lector intenta tomar un libro que ya está prestado."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class LibroNoEncontradoError(Exception):
    """Excepción lanzada cuando se intenta buscar o gestionar un libro que no está registrado en el sistema."""
    def __init__(self, mensaje):
        super().__init__(mensaje)


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
    def tomar_libro(self, libro: 'Libro'):
        if libro.estado == 'prestado':
            raise LibroNoDisponibleError(f"El libro {libro.titulo} no está disponible.")
        libro.estado = 'prestado'
        self.libros_prestados.append(libro)
        
    def devolver_libro(self, libro: 'Libro'):
        if libro not in self.libros_prestados:
            raise ValueError(f"No puedes devolver un libro que no has tomado.")     #Eliminar de la lista de libros prestados(Lector)
        libro.estado = 'disponible'
        self.libros_prestados.remove(libro)
        
    def __str__(self):
        return f"Lector: {self.nombre} (Id: {self.id}"

class Administrador(Usuario):
    @staticmethod
    def agregar_libro(libro: 'Libro', libros):
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
    
@dataclass    
class Prestamo:
    lector: 'Lector'
    libro: 'Libro'
    fecha_prestamo: datetime = field(default=None, init=False)
    _fecha_devolucion: datetime = field(default=None, init=False)
    
    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion       #Devuelve la fecha de devolución
    
    @fecha_devolucion.setter
    def fecha_devolucion(self, nueva_fecha: datetime):
        if nueva_fecha < self.fecha_prestamo:
            raise ValueError(f"La fecha de devolución no puede ser anterior a la fecha de préstamo.")
        self._fecha_devolucion = nueva_fecha
    
    def registrar_prestamo(self):
        self.libro.estado = 'prestado'
        print(f"Préstamo registrado: {self.lector.nombre} ha tomado '{self.libro.titulo}' el {self.fecha_prestamo}.")
        
    def devolver_libro(self):
        if self.libro.estado == 'disponible':
            raise ValueError(f"El libro '{self.libro.titulo}' ya está disponible.")
        self.fecha_devolucion = datetime.now()         # Establece la fecha de devolución a la fecha actual
        self.libro.estado = 'disponible'            # Cambia el estado del libro a disponible
        print(f"El libro '{self.libro.titulo}' ha sido devuelto el {self.fecha_devolucion}.")
    
    def __str__(self):
        return (f"Préstamo de '{self.libro.titulo}' a {self.lector.nombre} "
                f"desde {self.fecha_prestamo} hasta {self.fecha_devolucion if self.fecha_devolucion else 'en curso'}")
    
    
        
