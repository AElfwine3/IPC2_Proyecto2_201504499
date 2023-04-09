from Compuestos import CompuestosSingleton
from Maquinas import MaquinasSingleton


lista_compuestos = CompuestosSingleton.CompuestosSingleton.getInstance()
lista_maquinas = MaquinasSingleton.MaquinasSingleton.getInstance()

def analizar_compuesto(compuesto):
    elementos_compuesto = lista_compuestos.buscar_compuesto(compuesto)
    for i in range(lista_maquinas.tamanio()):
        pines_maquina = lista_maquinas.recorrer(i)
        for j in range(pines_maquina.tamanio()):
            elementos_pin = pines_maquina.recorrer(j)
            
            
