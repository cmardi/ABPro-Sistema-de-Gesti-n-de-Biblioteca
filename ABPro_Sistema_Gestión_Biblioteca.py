from dataclasses import dataclass


class LibroNoDisponibleError(Exception):
    """Clase para manejar el error de libro no disponible"""

    pass


class LibroNoEncontradoError(Exception):
    """Clase para manejar el error de libro no encontrado"""

    pass


class LibroNoEncontradoEnUsuarioError(Exception):
    """Excepción para cuando un libro no se encuentra en el usuario."""

    pass


class Usuario:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @staticmethod
    def validar_id_usr(idValidacion):
        return idValidacion.isdigit()

    @classmethod
    def contar_usuario(cls):
        pass


class Lector(Usuario):
    def __init__(self, id, nombre, libros):
        super().__init__(id, nombre)
        self._libros = libros

    def pedir_prestamo(self, libro):
        self._libros.append(libro)

    def devolver_prestamo(self, libro):
        self._libros.remove(libro)


class Administrador(Usuario):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    @staticmethod
    def agregar_libros(libro):
        Inventario.agregar_libro()


class LectorAdministrador(Lector, Administrador):
    pass


class Libro:
    def __init__(self, codigo, titulo, autor, estado):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._estado = estado

    def __str__(self):
        return f"Codigo: {self._codigo}, Titulo: {self._titulo}, Autor: {self._autor}, Estado: {self._estado}"

    def __repr__(self):
        return f"Libro('{self._codigo}', '{self._titulo}', '{self._autor} ','{self._estado}')"

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @classmethod
    def contar_libro(cls):
        pass


class Prestamo:
    def __init__(self, lector, libro, fecha_prestamo, fecha_devolucion):
        self._lector = lector
        self._libro = libro
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    def __str__(self):
        return f"Lector: {self._lector}, Libro: {self._libro},Fecha de prestamo: {self._fecha_prestamo}, Fecha de devolucion: {self._fecha_devolucion}"

    def __repr__(self):
        return f"Prestamo('{self._lector}', '{self._libro}', '{self._fecha_prestamo}', '{self._fecha_devolucion}')"

    def validar_fecha_dev(self, fecha_prestamo, fecha_devolucion):
        if fecha_prestamo > fecha_devolucion:
            return False
        else:
            return True

    def registrar_prestamo(self, usuario, libro, fecha_prestamo):
        self(usuario, libro, fecha_prestamo)

        Lector.pedir_prestamo(usuario, libro)
        print("Prestamo registrado con exito")

    def devolver_libro(self, usuario, libro, fecha_devolucion):
        if self.validar_fecha_dev(self._fecha_prestamo, fecha_devolucion):
            print("Fecha de devolucion es correcta")
            self._fecha_devolucion = fecha_devolucion
            print("Libro devuelto con exito")
            Lector.devolver_prestamo(usuario, libro)
        else:
            print("Fecha de devolucion no es correcta")


class Inventario:
    def __init__(self):
        self.libros = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def guardar_libro(self):
        try:
            with open("libros.txt", "w") as inventario:
                for libro in self.libros:
                    inventario.write(str(libro) + "\n")
        except Exception as e:
            print(f"Error al guardar el libro: {e}")

    def guardar_prestamo(self):
        try:
            with open("prestamos.txt", "w") as inventario:
                for prestamo in self.prestamos:
                    inventario.write(str(prestamo) + "\n")
        except Exception as e:
            print(f"Error al guardar el prestamo: {e}")


inventario = Inventario()
libro = Libro(1, "arroz", "arrocera", "prestado")
prestamo = Prestamo(2, 4, "ayer", "hoy")
inventario.agregar_prestamo(prestamo)
print(inventario.prestamos)
inventario.agregar_libro(libro)
print(inventario.libros)
inventario.guardar_libro()
inventario.guardar_prestamo()
