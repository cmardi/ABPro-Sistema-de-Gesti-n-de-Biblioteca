from dataclasses import dataclass, field
from typing import List

@dataclass
class Usuario:
    nombre: str
    id: int
    prestamos: List['Préstamo'] = field(default_factory=list)
    
    def solicitar_prestamo(self, libro: Libro):
        if libro.prestar():
            prestamo = Prestamo(libro,self)
            self.prestamos.append(prestamo)
            return prestamo
        
    def devolver_libro(self, libro: Libro):
        for prestamo in self.prestamos:
            if prestamo.libro.id == libro.id:
                libro.devolver()
                self.prestamos.remove(prestamo)
                return True
        return False
    
    def __len__(self):
        return len(self.prestamos)
    
    def __str__(self):
        return f"Usuario: {self.nombre} (Id: {self.id}) - Préstamos: {len(self.prestamos)})"
    
class Lector:
    pass

class Administrador(Usuario):
    def agregar_libro(self, libro: Libro, libros: List[Libro]):
        libros.append(libro)
        
    def eliminar_libro(self, id_libro: int, libros: List[Libro]):
        libros[:] = [libro for libro in libros if libro.id != id_libro]  
