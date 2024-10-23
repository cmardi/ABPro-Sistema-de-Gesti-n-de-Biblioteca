from dataclasses import dataclass
import os
import time

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
    def contar_usuarios(cls):
        return cls.contador_usuarios
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

        self.__libros_prestados = []#Encapsulacion usuario

    #Property para gestionar la lista de libros prestados
    @property
    def libros_prestados(self): 
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
            self.__libros_prestados.remove(libro)
            libro.estado = "disponible"


class Administrador(Usuario):
    catalogo = []

    @staticmethod
    def agregar_libro(libro):
        Administrador.catalogo.append(libro)
        Administrador.guardar_libro(libro)

    @staticmethod
    def guardar_libro(libro, archivo="libros.txt"):
        with open(archivo, 'a') as f:
            f.write(f"{libro.titulo},{libro.autor},{libro.codigounico},{libro.estado}\n")
        print("Libro guardado con éxito!")

    @staticmethod
    def eliminar_libro(libro, archivo="libros.txt"):
        if libro in Administrador.catalogo:
            Administrador.catalogo.remove(libro)
            # Actualizar el archivo después de eliminar el libro
            Administrador.actualizarlibrosarchivo(archivo)
            print(f"Libro '{libro.titulo}' eliminado del catálogo y del archivo.")
            return True
        else:
            print(f"El libro '{libro.titulo}' no se encuentra en el catálogo.")
            return False
    
    @staticmethod
    def actualizarlibrosarchivo(archivo="libros.txt"):
        # Sobrescribir todo el archivo con el catálogo actualizado
        with open(archivo, 'w') as f:
            for libro in Administrador.catalogo:
                f.write(f"{libro.titulo},{libro.autor},{libro.codigounico},{libro.estado}\n")
        print("Archivo actualizado con éxito!")
    
    @staticmethod
    def cargar_libros(archivo="libros.txt"):
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                Administrador.catalogo = []  # Limpiar el catálogo actual
                for linea in f:
                    titulo, autor, codigounico, estado = linea.strip().split(',')
                    libro = Libro(titulo, autor, int(codigounico), estado)
                    Administrador.catalogo.append(libro)
            print("Catálogo cargado con éxito.")
        else:
            print("El archivo de libros no existe.")

class LectorAdminsitrador(Lector, Administrador):
    def __init__(self, nombre, id):
        super().__init__(nombre, id)
    #Hereda las capacidades de las clases Lector/Adminsitrador

@dataclass
class Libro():
    titulo : str
    autor : str
    codigounico : int
    estado: str = "disponible"

    # def estado_libro():
    #     pass

    # def contar_libros():
    #     pass

    #Metodos Dunder de Libro
    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Estado: {self.estado}"

    def __repr__(self):
        return f"Libro(titulo={self.titulo}, autor={self.autor}, codigo={self.codigounico}, estado={self.estado})"
    

class Prestamo:
    @staticmethod
    def registrar_prestamo(lector, libro, archivo="prestamos.txt"):
        fecha = time.strftime("%Y-%m-%d %H:%M:%S")  #Formato de fecha usando time
        modo = 'a' if os.path.exists(archivo) else 'w'
        with open(archivo, modo) as f:
            f.write(f"{lector.id},{libro.codigounico},{fecha},pendiente\n")

    @staticmethod
    def registrar_devolucion(lector, libro, archivo="prestamos.txt"):
        fecha = time.strftime("%Y-%m-%d %H:%M:%S")  #Formato de fecha usando time
        prestamos = []
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                prestamos = f.readlines()
        
        with open(archivo, 'w') as f:
            for prestamo in prestamos:
                if f"{lector.id},{libro.codigounico}" in prestamo and "pendiente" in prestamo:
                    f.write(f"{lector.id},{libro.codigounico},{prestamo.split(',')[2]},{fecha}\n")
                else:
                    f.write(prestamo)


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


def main():
    Administrador.cargar_libros()
    libro1 = Libro("Quijote", "Martin", 1, "disponible")
    libro2 =  Libro("Papelucho", "Marcela", 2, "disponible")
    while True:
        print("\n Bienvenidos al Sistema de Gestión de Biblioteca")
        usuario = input("Ingresa tu tipo de Usuario(admin o lector): ")
        if usuario == "admin":
            print("1. Agregar un nuevo libro")#Admin
            print("2. Eliminar un libro")#Admin
            print("3. Libros disponibles en Biblioteca")
            print("4. Salir")
            opcionadmin = input("Selecciona una de las opciones(Admin):")
            while True:
                if opcionadmin == '1':
                    Administrador.agregar_libro(libro1)
                    Administrador.agregar_libro(libro2)
                    #Ingresar el libro
                elif opcionadmin == '2':
                    Administrador.eliminar_libro(libro2)
                    #Eliminar el libro
                elif opcionadmin == '3':
                    print("Mostrar Lirbos")
                    Administrador.catalogo()
                elif opcionadmin == "4":
                        break
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
                break
        elif usuario == "lector":
            print("1. Solicitar préstamo de libro")#Lector
            print("2. Devolver libros")#Lector  
            print("3. Ver lista de préstamos")#Lista de prestamos en Prestamo

            opcionlector = input("Selecciona una de las opciones(Lector):")

            if opcionlector == '1':
                # Solicitar los datos del nuevo libro
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                codigo = int(input("Ingrese el código único del libro: "))
                nuevo_libro = Libro(titulo, autor, codigo)
                Administrador.agregar_libro(nuevo_libro)
            elif opcionlector == '2':
                # Eliminar libro
                titulo = input("Ingrese el título del libro a eliminar: ")
                libro_a_eliminar = next((libro for libro in Administrador.catalogo if libro.titulo == titulo), None)
                if libro_a_eliminar:
                    Administrador.eliminar_libro(libro_a_eliminar)
                else:
                    print(f"El libro '{titulo}' no se encuentra en el catálogo.")
            elif opcionlector == '3':

                if opcionlector == "1":
                    print("\nLibros disponibles:")
                    libros_disponibles = [l for l in Administrador.catalogo if l.estado == "disponible"]
                    for i, libro in enumerate(libros_disponibles):
                        print(f"{i+1}. {libro}")
            break

main()