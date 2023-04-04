import Pin

class ListaPin:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0

    def Insertar(self, elementos, numero_pines):
        if self._tamanio >= numero_pines:
            print('El numero de pines es mayor al numero de pines que acepta la maquina')
            return
        nuevo_pin = Pin.Pin(elementos)
        if self.cabeza == None:
            self.cabeza = nuevo_pin
            self.cola = nuevo_pin
        else:
            nuevo_pin.anterior = self.cola
            self.cola.siguiente = nuevo_pin
            self.cola = nuevo_pin
        self._tamanio += 1
    
    def verificar_elementos(self, elementos):
        aux = self.cabeza
        while aux is not None:
            if aux.verificar_elementos(elementos):
                return True
            aux = aux.siguiente
        return False
