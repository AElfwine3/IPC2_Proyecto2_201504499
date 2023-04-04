
class Pin:

    def __init__(self, elementos):
        self._elementos = elementos
        self.siguiente = None
        self.anterior = None

    def verificar_elementos(self, elementos):
        if self._elementos == elementos:
            return True
        else:
            return False