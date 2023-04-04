import Elementos.TablaElementos as TablaElementos


class ElementosSingleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ElementosSingleton.__instance == None:
            ElementosSingleton()
        return ElementosSingleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ElementosSingleton.__instance != None:
            raise Exception("Ya existe una instancia de Elementos!")
        else:
            ElementosSingleton.__instance = TablaElementos.TablaElementos()