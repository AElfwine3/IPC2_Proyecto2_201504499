import Compuestos.ListaCompuestos as ListaCompuestos

class CompuestosSingleton:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if CompuestosSingleton.__instance == None:
            CompuestosSingleton()
        return CompuestosSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if CompuestosSingleton.__instance != None:
            raise Exception("Ya existe una instancia de Compuestos!")
        else:
            CompuestosSingleton.__instance = ListaCompuestos.ListaCompuestos()