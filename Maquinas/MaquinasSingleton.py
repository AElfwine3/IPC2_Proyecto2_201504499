import Maquinas.ListaMaquinas as ListaMaquinas

class MaquinasSingleton:

    __instance = None

    @staticmethod
    def getInstance():
        if MaquinasSingleton.__instance is None:
            MaquinasSingleton()
        return MaquinasSingleton.__instance

    def __init__(self):
        if MaquinasSingleton.__instance is not None:
            raise Exception("Ya existe una instancia de Maquinas!")
        else:
            MaquinasSingleton.__instance = ListaMaquinas.ListaMaquinas()