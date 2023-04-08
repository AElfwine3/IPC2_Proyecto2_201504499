import xml.etree.ElementTree as ET
from Elementos import ElementosSingleton, TablaElementos
from Compuestos import CompuestosSingleton
from Maquinas import ListaPin, MaquinasSingleton


tabla_elementos = ElementosSingleton.ElementosSingleton.getInstance()
lista_compuestos = CompuestosSingleton.CompuestosSingleton.getInstance()
lista_maquinas = MaquinasSingleton.MaquinasSingleton.getInstance()

def agregar_elemento(elemento, numero_atomico='', simbolo='', nombre=''):
    if elemento.tag == 'elemento':
        for atributo in elemento:
            if atributo.tag == 'numeroAtomico':
                numero_atomico = atributo.text
            elif atributo.tag == 'simbolo':
                simbolo = atributo.text
            elif atributo.tag == 'nombreElemento':
                nombre = atributo.text
        if numero_atomico != '' and simbolo != '' and nombre != '':
            tabla_elementos.insertar(numero_atomico, simbolo, nombre)
    for objeto in elemento:
        agregar_elemento(objeto)

def agregar_maquina(maquina):
    nombre = ''
    numero_pines = 0
    numero_elementos = 0
    pines = ListaPin.ListaPin()
    for atributo in maquina:
        print(f'{atributo.tag} {atributo.text}')
        if atributo.tag == 'nombre':
            nombre = atributo.text
        elif atributo.tag == 'numeroPines':
            numero_pines = atributo.text
        elif atributo.tag == 'numeroElementos':
            numero_elementos = atributo.text
        elif atributo.tag == 'pin':
            pin_elementos = TablaElementos.TablaElementos()
            for elementos in atributo:
                for elemento in elementos:
                    if pin_elementos.verificar_elemento(elemento.text):
                        print('El elemento ya existe en este pin')
                        return
                    if pines.verificar_elementos(elemento.text):
                        print('El elemento ya existe en otro pin')
                        return
                    print(f'{elemento.tag} {elemento.text}')
                    elemento_pin = tabla_elementos.buscar(elemento.text)
                    if elemento_pin is not None:
                        pin_elementos.insertar_compuesto(elemento_pin)
            pines.insertar(pin_elementos, int(numero_pines))
    if nombre != '' and numero_pines != 0 and numero_elementos != 0 and pines is not None:
        lista_maquinas.agregar(nombre, numero_pines, numero_elementos, pines)
        print(lista_maquinas.imprimir())

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