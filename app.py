from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import webbrowser
from PIL import ImageTk, Image
from Controllers import LecturaArchivo, GraficarMaquinas
from Elementos import ElementosSingleton
from Compuestos import CompuestosSingleton
from Maquinas import MaquinasSingleton


tabla_elementos = ElementosSingleton.ElementosSingleton.getInstance()
lista_compuestos = CompuestosSingleton.CompuestosSingleton.getInstance()
lista_maquinas = MaquinasSingleton.MaquinasSingleton.getInstance()

class App:
    def __init__(self, root):
        self.root = root

        self.style = ttk.Style(self.root)
        self.root.tk.call('source', 'Temas/forest-dark.tcl')
        self.style.theme_use('forest-dark')

        self.root.title("Sistema de Gestion de Quimicos")
        self.root.geometry("850x700")
        # self.root.resizable(0,0)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Abrir", command=self.load)
        self.file_menu.add_command(label="Generar", command=self.generate)
        self.menu.add_cascade(label="Archivo", menu=self.file_menu)
        
        self.title = Label(self.root, text="Sistema de Gestion de Inventarios", font=("Arial", 20))
        self.title.place(x=200, y=20)

        self.grid = Frame(self.root, width=700, height=500)
        self.grid.place(x=50, y=100)

        self.tab_frame = ttk.Notebook(self.grid)
        self.tab_frame.grid(row=1, column=0)

        self.tab_frame.bind("<<NotebookTabChanged>>", self.tab_changed)

        self.tab1 = ttk.Frame(self.tab_frame)
        self.tab_frame.add(self.tab1, text="Inicializar")
        self.tab2 = ttk.Frame(self.tab_frame)
        self.tab_frame.add(self.tab2, text="Gestion de elementos")
        self.tab3 = ttk.Frame(self.tab_frame)
        self.tab_frame.add(self.tab3, text="Gestion de compuestos")
        self.tab4 = ttk.Frame(self.tab_frame)
        self.tab_frame.add(self.tab4, text="Gestion de maquinas")
        self.tab5 = ttk.Frame(self.tab_frame)
        self.tab_frame.add(self.tab5, text="Ayuda")
    
    def tab_changed(self, event):
        print("Tab changed")
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")

        if tab_text == "Inicializar":
            self.init()
        elif tab_text == "Gestion de elementos":
            self.elements()
        elif tab_text == "Gestion de compuestos":
            self.compounds()
        elif tab_text == "Gestion de maquinas":
            self.machines()
        elif tab_text == "Ayuda":
            self.help()

    def init(self):
        self.frame = Frame(self.tab1, width=700, height=400)
        self.frame.grid(row=0, column=0)
        self.title = Label(self.frame, text="Bienvenido", font=("Arial", 20))
        self.title.place(x=270, y=25)
        self.text = Label(self.frame, text="Para comenzar, seleccione un archivo XML desde el menu archivo", font=("Arial", 12))
        self.text.place(x=125, y=75)
    
    def load(self):
        self.file = filedialog.askopenfile(title="Selecciona un archivo", mode='r', filetypes=(("Archivos XML", "*.xml"),))
        if self.file is not None:
            LecturaArchivo.leer_xml(self.file)
            self.file.close()
    
    def generate(self):
        print("Generar archivo")
    
    def elements(self):
        self.frame = ttk.Frame(self.tab2, width=600, height=400)
        self.frame.grid(row=0, column=0)
        
        self.title = ttk.Label(self.frame, text="Elementos", font=("Arial", 20))
        self.title.grid(row=0, column=0)

        self.element_frame = ttk.LabelFrame(self.frame, text="Agregar Elemento")
        self.element_frame.grid(row=1, column=0, padx=10, pady=5)

        self.numero_entry = ttk.Entry(self.element_frame)
        self.numero_entry.insert(0, "Numero Atomico")
        self.numero_entry.bind("<FocusIn>", lambda event: self.numero_entry.delete(0, END))
        self.numero_entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.simbolo_entry = ttk.Entry(self.element_frame)
        self.simbolo_entry.insert(0, "Simbolo")
        self.simbolo_entry.bind("<FocusIn>", lambda event: self.simbolo_entry.delete(0, END))
        self.simbolo_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        self.nombre_entry = ttk.Entry(self.element_frame)
        self.nombre_entry.insert(0, "Nombre")
        self.nombre_entry.bind("<FocusIn>", lambda event: self.nombre_entry.delete(0, END))
        self.nombre_entry.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.element_btn = ttk.Button(self.element_frame, text="Agregar", command=self.add_element)
        self.element_btn.grid(row=3, column=0, sticky="nsew" , padx=5, pady=5)

        self.tree_frame = ttk.Frame(self.frame, height=300)
        self.tree_frame.grid(row=1, column=1, padx=1, pady=5)

        treescrolly = ttk.Scrollbar(self.tree_frame, orient="vertical")
        treescrolly.pack(side="right", fill="y")

        columns = ("Numero atomico", "Simbolo", "Nombre")
        self.tree = ttk.Treeview(self.tree_frame, show="headings", columns=columns, yscrollcommand=treescrolly.set)
        self.tree.column("Numero atomico", width=100)
        self.tree.column("Simbolo", width=75)
        self.tree.column("Nombre", width=200)
        self.tree.heading("Numero atomico", text="Numero atomico")
        self.tree.heading("Simbolo", text="Simbolo")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.pack(side="left", fill="both")
        treescrolly.config(command=self.tree.yview)

        tabla_elementos.crear_lista(self.tree)

        GraficarMaquinas.graficar_elementos()
    
    def compounds(self):
        self.frame = Frame(self.tab3, width=600, height=400)
        self.frame.grid(row=0, column=0)
        self.title = Label(self.frame, text="Compuestos", font=("Arial", 20))
        self.title.grid(row=0, column=0)

        self.tree_frame = ttk.Frame(self.frame, height=300)
        self.tree_frame.grid(row=0, column=0, padx=5, pady=5)

        treescrolly = ttk.Scrollbar(self.tree_frame, orient="vertical")
        treescrolly.pack(side="right", fill="y")

        self.tree_compound = ttk.Treeview(self.tree_frame, yscrollcommand=treescrolly.set)
        self.tree_compound.heading("#0", text="Nombre")
        self.tree_compound.pack(side="left", fill="both")
        self.tree_compound.bind("<<TreeviewSelect>>", self.on_tree_select)
        treescrolly.config(command=self.tree_compound.yview)

        lista_compuestos.crear_lista(self.tree_compound)

        print(lista_compuestos.imprimir())
    
    def on_tree_select(self, event):
        tree = event.widget
        selection = [tree.item(item)["text"] for item in tree.selection()]

        self.tree_frame = ttk.Frame(self.frame, height=300)
        self.tree_frame.grid(row=0, column=1, padx=10, pady=5)

        treescrolly = ttk.Scrollbar(self.tree_frame, orient="vertical")
        treescrolly.pack(side="right", fill="y")

        columns = ("Numero atomico", "Simbolo", "Nombre")
        self.tree_comp = ttk.Treeview(self.tree_frame, show="headings", columns=columns, yscrollcommand=treescrolly.set)
        self.tree_comp.column("Numero atomico", width=100)
        self.tree_comp.column("Simbolo", width=75)
        self.tree_comp.column("Nombre", width=200)
        self.tree_comp.heading("Numero atomico", text="Numero atomico")
        self.tree_comp.heading("Simbolo", text="Simbolo")
        self.tree_comp.heading("Nombre", text="Nombre")
        self.tree_comp.pack(side="left", fill="both")
        treescrolly.config(command=self.tree_comp.yview)

        seleccion = ''.join(selection)
        lista_compuestos.buscar(seleccion, self.tree_comp)
    
    def machines(self):
        self.frame = Frame(self.tab4, width=600, height=400)
        self.frame.grid(row=0, column=0)
        self.title = Label(self.frame, text="Maquinas", font=("Arial", 20))
        self.title.grid(row=0, column=0)

        # self.tree_frame = ttk.Frame(self.frame, height=300)
        # self.tree_frame.grid(row=0, column=0, padx=5, pady=5)
        # treescrolly = ttk.Scrollbar(self.tree_frame, orient="vertical")
        # treescrolly.pack(side="right", fill="y")
        # columns = ("Nombre", "Numero pines", "Numero elementos")
        # self.tree_machine = ttk.Treeview(self.tree_frame, show="headings", columns=columns, yscrollcommand=treescrolly.set)
        # self.tree_machine.column("Nombre", width=125)
        # self.tree_machine.column("Numero pines", width=100)
        # self.tree_machine.column("Numero elementos", width=125)
        # self.tree_machine.heading("Nombre", text="Nombre")
        # self.tree_machine.heading("Numero pines", text="Numero de pines")
        # self.tree_machine.heading("Numero elementos", text="Numero de elementos")
        # self.tree_machine.pack(side="left", fill="both")
        # treescrolly.config(command=self.tree_machine.yview)
        # lista_maquinas.crear_lista(self.tree_machine)

        GraficarMaquinas.graficar()

        # self.img_frame = ttk.Frame(self.frame, width= 200, height=300)
        # self.img_frame.grid(row=1, column=0, padx=10, pady=5)

        self.load = Image.open("Maquinas.png")
        self.load = self.load.resize((700, 250), Image.LANCZOS)
        self.render = ImageTk.PhotoImage(self.load)
        self.img = ttk.Label(self.frame, image=self.render)
        self.img.grid(row=0, column=0, padx=10, pady=5)

    
    def help(self):
        self.frame = Frame(self.tab5, width=600, height=400)
        self.frame.place(x=160, y=30)
        self.title = Label(self.frame, text="Ayuda", font=("Arial", 20))
        self.title.grid(row=0, column=0, padx=10, pady=20)

        self.text = Label(self.frame, text="Introduccion a la Programacion y Computacion 2 C", font=("Arial", 12))
        self.text.grid(row=1, column=0)
        self.text = Label(self.frame, text="Elvin Leonel Mayen Carrillo", font=("Arial", 12))
        self.text.grid(row=2, column=0)
        self.text = Label(self.frame, text="201504499", font=("Arial", 12))
        self.text.grid(row=3, column=0)

        self.docu = ttk.Button(self.frame, text="Ver Documentacion", command=self.documentacion)
        self.docu.grid(row=4, column=0, padx=10, pady=20)

    def documentacion(self):
        webbrowser.open("https://github.com/AElfwine3/IPC2_Proyecto2_201504499/blob/main/Documentacion/ArticuloEnsayo-IPC2-lab.pdf")
    
    def add_element(self):
        print('Agregar elemento')
        numero = self.numero_entry.get()
        simbolo = self.simbolo_entry.get()
        nombre = self.nombre_entry.get()
        if numero != "" and simbolo != "" and nombre != "":
            tabla_elementos.insertar(numero, simbolo, nombre)
            self.tree.delete(*self.tree.get_children())
            tabla_elementos.crear_lista(self.tree)
            self.numero_entry.delete(0, END)
            self.simbolo_entry.delete(0, END)
            self.nombre_entry.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()