import Maquinas.Maquina as Maquina

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
    
    def imprimir(self):
        aux = self.primero
        while aux is not None:
            print(aux)
            aux = aux.siguiente

    def crear_lista(self, lista):
        aux = self.primero
        while aux is not None:
            aux.mostrar_en_lista(lista)
            aux = aux.siguiente

    def tamano(self):
        return self.tamanio
    
    def recorrer(self, indice):
        nodo_actual = self.primero
        contador = 0
        while nodo_actual is not None:
            if contador == indice:
                return nodo_actual
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return None
