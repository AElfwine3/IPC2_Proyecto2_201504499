
class Maquina:

    def __init__(self, nombre, numero_pines, numero_elementos, lista_pines):
        self._nombre = nombre
        self._numero_pines = numero_pines
        self._limite_elementos = numero_elementos
        self._lista_pines = lista_pines
        self.siguiente = None

    def verificar_nombre(self, nombre):
        return self._nombre == nombre
    
    def __str__(self) -> str:
        return f'Nombre: {self._nombre} - Pines: {self._lista_pines.imprimir()}'