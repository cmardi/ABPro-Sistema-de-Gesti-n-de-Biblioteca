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