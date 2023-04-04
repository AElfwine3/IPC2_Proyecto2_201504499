
class Elemento:
    
    def __init__(self, numero_atomico, simbolo, nombre):
        self._numero_atomico = numero_atomico
        self._simbolo = simbolo
        self._nombre = nombre
        self.siguiente = None
    
    def verificar_simbolo(self, simbolo):
        if self._simbolo == simbolo:
            return True
        return False
    
    def verificar_numero_atomico(self, numero_atomico):
        if self._numero_atomico == numero_atomico:
            return True
        return False
    
    def verificar_nombre(self, nombre):
        if self._nombre == nombre:
            return True
        return False
    
    def mostrar_en_lista(self, lista):
        lista.insert('', 'end', values=(self._numero_atomico, self._simbolo, self._nombre))
    
    def __str__(self):
        return f'Numero atomico: {self._numero_atomico}, Simbolo: {self._simbolo}, Nombre: {self._nombre}'