import Compuestos.Compuesto as Compuesto

class ListaCompuestos:
    
        def __init__(self):
            self.primero = None
            self.tamanio = 0
    
        def agregar(self, nombre, elementos):
            if self.verificar_compuesto(nombre):
                return
            compuesto = Compuesto.Compuesto(nombre, elementos)
            if self.primero is None:
                self.primero = compuesto
            else:
                aux = self.primero
                while aux.siguiente is not None:
                    aux = aux.siguiente
                aux.siguiente = compuesto
            self.tamanio += 1
        
        def buscar(self, nombre, lista):
            aux = self.primero
            while aux is not None:
                if aux.verificar_nombre(nombre):
                    aux.lista_elementos(lista)
                    return
                aux = aux.siguiente
            return None
        
        def verificar_compuesto(self, nombre):
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
        