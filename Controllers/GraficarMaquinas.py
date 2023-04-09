import os
import random
from Maquinas import MaquinasSingleton
from Elementos import ElementosSingleton

lista_maquinas = MaquinasSingleton.MaquinasSingleton.getInstance()
tabla_elementos = ElementosSingleton.ElementosSingleton.getInstance()

def graficar():
    with open('Maquinas.dot', mode='w') as grafica:
        grafica.write('digraph Maquinas{\n')
        grafica.write('\trankdir=LR;\n')
        grafica.write('\tfontname="Helvetica,Arial,sans-serif"\n')
        grafica.write('\tnode [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\tedge [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\ta0 [shape=none label=<\n')
        grafica.write('\t<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="8" CELLPADDING="8">\n')
        for i in range(lista_maquinas.tamanio):
            maquina = lista_maquinas.recorrer(i)
            grafica.write('\t\t<TR>\n')
            grafica.write(f'\t\t\t<TD style="radial" bgcolor="#F7F7FF:#B9C0DA"> {maquina._nombre} </TD>\n')
            grafica.write('\t\t</TR>\n')
            for j in range(maquina._lista_pines._tamanio):
                elementos_pin = maquina._lista_pines.recorrer(j)
                grafica.write('\t\t<TR>\n')
                grafica.write(f'\t\t\t<TD> Pin {j+1} </TD>\n')
                for k in range(elementos_pin.tamanio):
                    elemento = elementos_pin.recorrer(k)
                    grafica.write(f'\t\t\t<TD bgcolor="#B9C0DA:{asignar_color()}" gradientangle="90"> {elemento._numero_atomico}<BR/>{elemento._simbolo}<BR/>{elemento._nombre} </TD>\n')
                grafica.write('\t\t</TR>\n')
        grafica.write('\t</TABLE>>];\n')
        grafica.write('}')
        grafica.close()

        os.system('dot -Tpng Maquinas.dot -o Maquinas.png')
        # os.system('start Maquinas.png')

def graficar_elementos():
    with open('Elementos.dot', mode='w') as grafica:
        grafica.write('digraph Elementos{\n')
        grafica.write('\trankdir=LR;\n')
        grafica.write('\tfontname="Helvetica,Arial,sans-serif"\n')
        grafica.write('\tnode [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\tedge [fontname="Helvetica,Arial,sans-serif"]\n')
        grafica.write('\ta0 [shape=none label=<\n')
        grafica.write('\t<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="1" CELLPADDING="8">\n')
        grafica.write('\t\t<TR>\n')
        grafica.write(f'\t\t\t<TD style="radial" bgcolor="#F7F7FF:#B9C0DA" colspan="3"> Tabla Elementos </TD>\n')
        grafica.write('\t\t</TR>\n')
        grafica.write('\t\t<TR>\n')
        grafica.write(f'\t\t\t<TD> Numero Atomico </TD>\n')
        grafica.write(f'\t\t\t<TD> Simbolo </TD>\n')
        grafica.write(f'\t\t\t<TD> Nombre </TD>\n')
        grafica.write('\t\t</TR>\n')
        for i in range(tabla_elementos.tamanio):
            elemento = tabla_elementos.recorrer(i)
            grafica.write('\t\t<TR>\n')
            grafica.write(f'\t\t\t<TD> {elemento._numero_atomico} </TD>\n')
            grafica.write(f'\t\t\t<TD> {elemento._simbolo} </TD>\n')
            grafica.write(f'\t\t\t<TD> {elemento._nombre} </TD>\n')
            grafica.write('\t\t</TR>\n')
        grafica.write('\t</TABLE>>];\n')
        grafica.write('}')
        grafica.close()

        os.system('dot -Tpng Elementos.dot -o Elementos.png')
        os.system('start Elementos.png')

def asignar_color():
        for i in range(3):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        return hex_color
