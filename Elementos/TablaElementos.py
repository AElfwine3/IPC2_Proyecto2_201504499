import Elementos.Elemento as Elemento


class TablaElementos:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def insertar(self, numero_atomico, simbolo, nombre):
        if self.verificar_elemento(simbolo, numero_atomico, nombre):
            print('El elemento ya existe')
            return
        elemento = Elemento.Elemento(numero_atomico, simbolo, nombre)
        if self.primero == None:
            self.primero = elemento
            self.ultimo = elemento
        else:
            elemento.anterior = self.ultimo
            self.ultimo.siguiente = elemento
            self.ultimo = elemento
        self.tamanio += 1
    
    def insertar_compuesto(self, nodo):
        elemento = Elemento.Elemento(nodo._numero_atomico, nodo._simbolo, nodo._nombre)
        if self.primero is None:
            self.primero = elemento
        else:
            aux = self.primero
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = elemento
        self.tamanio += 1
    
    def buscar(self, simbolo):
        aux = self.primero
        while aux is not None:
            if aux.verificar_simbolo(simbolo):
                return aux
            aux = aux.siguiente
        return None
    
    def verificar_elemento(self, simbolo, numero_atomico = None, nombre = None):
        aux = self.primero
        while aux is not None:
            if aux.verificar_simbolo(simbolo) or aux.verificar_numero_atomico(numero_atomico) or aux.verificar_nombre(nombre):
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
        return lista
    
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