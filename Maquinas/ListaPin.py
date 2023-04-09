import Maquinas.Pin as Pin

class ListaPin:
    
    def __init__(self):
        self.cabeza = None
        self._tamanio = 0

    def insertar(self, elementos, numero_pines):
        if self._tamanio >= numero_pines:
            print('Maximo numero de pines alcanzado')
            return
        nuevo_pin = Pin.Pin(elementos)
        if self.cabeza is None:
            self.cabeza = nuevo_pin
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo_pin
        self._tamanio += 1
    
    def verificar_elementos(self, elemento):
        aux = self.cabeza
        while aux is not None:
            if aux.verificar_elementos(elemento):
                return True
            aux = aux.siguiente
        return False
    
    def imprimir(self):
        aux = self.cabeza
        while aux is not None:
            print(aux)
            aux = aux.siguiente
        
    def tamano(self):
        return self._tamanio
    
    def recorrer(self, indice):
        nodo_actual = self.cabeza
        contador = 0
        while nodo_actual is not None:
            if contador == indice:
                return nodo_actual._elementos
            contador += 1
            nodo_actual = nodo_actual.siguiente
