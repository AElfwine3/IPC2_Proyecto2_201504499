import Maquina

class ListaMaquinas:

    def __init__(self):
        self.primero = None
        self.tamanio = 0

    def agregar(self, nombre, numero_pines, numero_elementos, lista_pines):
        if self.verificar_maquina(nombre):
            return
        maquina = Maquina.Maquina(nombre, numero_pines, numero_elementos, lista_pines)
        if self.primero is None:
            self.primero = maquina
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = maquina
        self.tamanio += 1
    
    def buscar(self, nombre):
        aux = self.primero
        while aux is not None:
            if aux.verificar_nombre(nombre):
                return aux
            aux = aux.siguiente
        return None
    
    def verificar_maquina(self, nombre):
        aux = self.primero
        while aux is not None:
            if aux.verificar_nombre(nombre):
                return True
            aux = aux.siguiente
        return False