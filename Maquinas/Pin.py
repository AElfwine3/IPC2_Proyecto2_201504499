
class Pin:

    def __init__(self, elementos):
        self._elementos = elementos
        self.siguiente = None

    def verificar_elementos(self, elemento):
        if self._elementos.verificar_elemento(elemento):
            return True
        return False
    
    def __str__(self):
        return f'Elementos: {self._elementos.imprimir()}'