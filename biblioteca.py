from dataclasses import dataclass
import os

class LibroNoDisponibleError(Exception):
    pass
class LibroNoEncontradoError(Exception):
    pass

@dataclass
class Usuario:
    nombre : str
    id : int
    contador_usuarios = 0
    
    def obtener_nombre (self):
        return self.nombre
    
    def obtener_id (self):
        return self.id

    @staticmethod
    def validar_id(id):
        #Logica para validar id
        pass

    #para sumar 1 cada vez que se cree un usuario
    def __post_init__(self):
        Usuario.contador_usuarios += 1

    @classmethod
    def contar_usuarios(contador_usuarios):
        return contador_usuarios
    #print(contador_usuarios)
        
    #Formato de cadena legible.
    def __str__(self):
        return f"Usuario: {self.nombre}, Id: {self.id}"
    
    #Representación adecuada para depuración.
    def __repr__(self):
        return f"Usuario(nombre:{self.nombre}, Id:{self.id})"


class Lector(Usuario):
    def __init__(self,nombre, id):
        super().__init__(nombre, id)

        self.__libros_prestados = []#Encapsulacion

    #Property para gestionar la lista de libros prestados
    @property
    #def libros_prestados(self):
    def _libros_prestados(self):
        return self.__libros_prestados

    #Metodos de Instancia
    def tomar_libro(self, libro):
        if libro.estado == "disponible":
            self._libros_prestados.append(libro)
            libro.estado = "prestado"
            print(f"{libro} ")
        else:
            raise LibroNoDisponibleError(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        if libro not in self._libros_prestados:
            raise LibroNoEncontradoError(f"El libro {libro.titulo} no esta en la lista de prestamos")
        else:
            self._libros_prestados.remove(libro)
            libro.estado = "disponible"


class Adminsitrador(Usuario):
    catalogo = []

    @staticmethod
    def agregar_libro(libro):
        Adminsitrador.catalogo.append(libro)
        Adminsitrador.guardar_libro(libro)

    @staticmethod
    def guardar_libro(libro, archivo="libros.txt"):
        with open(archivo, 'w') as f:
                f.write(f"{libro.titulo},{libro.autor},{libro.codigounico},{libro.estado}\n")
        print("Libro Guardado con Exito!")

    def eliminar_libro(libro):
        if libro in Adminsitrador.catalogo:
            Adminsitrador.catalogo.remove(libro)
            Adminsitrador.actualizarlibrosarchivo()
            return True
        return False
    
    @staticmethod
    def actualizarlibrosarchivo(archivo="libros.txt"):
        with open(archivo, 'w') as f:
            for libro in Adminsitrador.catalogo:
                f.write(f"{libro.titulo},{libro.autor},{libro.codigounico},{libro.estado}\n")

    @classmethod
    def conteo_libros_disponiles(cls):
        return print(len(Adminsitrador.catalogo)) #Me falta ver cuales son tienen el estado disponible con un for
    

class LectorAdminsitrador(Lector, Adminsitrador):
    def __init__(self, nombre, id):
        super().__init__(nombre, id)
    #Hereda las capacidades de las clases Lector/Adminsitrador

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

    #Metodos Dunder de Libro
    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Estado: {self.estado}"

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, codigo={self.codigounico}, estado={self.estado})"
    


class Prestamo():
    pass


# #probando guardar libros
# libro =  Libro("Quijote", "Martin", 1, "disponible")
# libro2 =  Libro("Papelucho", "Marcela", 2, "disponible")

# Adminsitrador.agregar_libro(libro)
# Adminsitrador.guardar_libro(libro)

# Adminsitrador.agregar_libro(libro2)
# Adminsitrador.guardar_libro(libro2)


# # Adminsitrador.eliminar_libro(libro1)
# # print(Adminsitrador.catalogo)

# # Adminsitrador.conteo_libros_disponiles()
# lector1 = Lector("Simon", 10)
# lector1.tomar_libro(libro)
# print(Adminsitrador.catalogo)
