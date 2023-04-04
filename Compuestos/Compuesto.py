
class Compuesto:

    def __init__(self, nombre, elementos):
        self._nombre = nombre
        self._elementos = elementos
        self.siguiente = None
    
    def verificar_nombre(self, nombre):
        if self._nombre == nombre:
            return True
        return False
    
    def mostrar_en_lista(self, lista):
        lista.insert('', 'end', text=self._nombre)
    
    def lista_elementos(self, lista):
        self._elementos.crear_lista(lista)
    
    def __str__(self):
        return f'Nombre: {self._nombre} Elementos: {self._elementos.imprimir()}'