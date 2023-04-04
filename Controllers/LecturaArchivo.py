import xml.etree.ElementTree as ET
from Elementos import ElementosSingleton, TablaElementos
from Compuestos import CompuestosSingleton


tabla_elementos = ElementosSingleton.ElementosSingleton.getInstance()
lista_compuestos = CompuestosSingleton.CompuestosSingleton.getInstance()

def agregar_elemento(elemento, numero_atomico='', simbolo='', nombre=''):
    if elemento.tag == 'elemento':
        # atributos = {}
        for atributo in elemento:
            if atributo.tag == 'numeroAtomico':
                numero_atomico = atributo.text
            elif atributo.tag == 'simbolo':
                simbolo = atributo.text
            elif atributo.tag == 'nombreElemento':
                nombre = atributo.text
            # print(f'numero_atomico: {numero_atomico}, simbolo: {simbolo}, nombre: {nombre}')
            # atributos[atributo.tag] = atributo.text
        # if atributos:
        #     tabla_elementos.insertar(atributos.get('numeroAtomico'), atributos.get('simbolo'), atributos.get('nombreElemento'))
        if numero_atomico != '' and simbolo != '' and nombre != '':
            tabla_elementos.insertar(numero_atomico, simbolo, nombre)
    for objeto in elemento:
        agregar_elemento(objeto)

def agregar_maquina(maquina):
    for atributo in maquina:
        print(f'{atributo.tag} {atributo.text}')

def agregar_compuesto(compuesto):
    nombre = ''
    elementos = TablaElementos.TablaElementos()
    for atributo in compuesto:
        print(f'{atributo.tag} {atributo.text}')
        if atributo.tag == 'nombre':
            nombre = atributo.text
        elif atributo.tag == 'elementos':
            for elemento in atributo:
                elemento_compuesto = tabla_elementos.buscar(elemento.text)
                if elemento_compuesto is not None:
                    elementos.insertar_compuesto(elemento_compuesto)
    if nombre != '' and elementos is not None:
        lista_compuestos.agregar(nombre, elementos)

def lectura(objeto_xml):
    if objeto_xml.tag == 'listaElementos':
        agregar_elemento(objeto_xml)
    elif objeto_xml.tag == 'Maquina':
        agregar_maquina(objeto_xml)
    elif objeto_xml.tag == 'compuesto':
        agregar_compuesto(objeto_xml)
    for objeto in objeto_xml:
        lectura(objeto)

def leer_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    if not root.tag == "CONFIG":
        print("El archivo no pertenece a datos sobre Marte")
        return
    lectura(root)