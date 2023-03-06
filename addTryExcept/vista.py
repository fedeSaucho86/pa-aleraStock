from tkinter import StringVar  
from PIL import ImageTk, Image
from tkinter import DoubleVar 
from tkinter import IntVar
from tkinter import Label
from tkinter import ttk
from tkinter import Menu
from tkinter import CENTER
from tkinter import END
from tkinter import messagebox as MessageBox
from model import Modelo
from utils import Utils
from loggerService import loggerService 
from error_register import error_reg
from typing import Type, Any

class Vista():
    
    def __init__(self, root:Type[Any] = None) -> None:
        """
        Receive Tk() object and create app view

        Args:
            root (Type[Any], optional): Tk() object
        """
        self.model = Modelo()
        self.vista_principal(root)
        
    def message(self, msg:str = "", frase:str = "") -> None:
        """
        Generate info message in app view

        Args:
            msg (str, optional): message warning
            frase (str, optional): question itself
        """
        MessageBox.showinfo(msg, frase)

    def ask(self, msg:str = "", frase:str = "") -> None:
        """
        Generate ask message in app view

        Args:
            msg (str, optional): message question
            frase (str, optional): question itself
        """
        return MessageBox.askquestion(msg, frase, icon='warning')

    def clear_text (self, lista_entry:list = []) -> None:
        """
        Clear treeview after change

        Args:
            lista_entry (list, optional): list with entries
        """
        for entry in lista_entry:
            entry.delete(0, END)

    def actualizar_treeview(self, mitreview:Any, product:str = "") -> None:
        """
        Show in screen required information

        Args:
            mitreview (Any): Treeview object
            product (str, optional): Product Id
        """
        sql_query = self.model.consultar(product)  
        if not sql_query:
            self.message("Error","No existe el Producto")
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        mitreview.tag_configure('grey', background='lightgrey')
        mitreview.tag_configure('white', background='white')
        for i, fila in enumerate(sql_query):
            if i % 2 == 0:
                my_tag = 'grey' 
            else:
                my_tag = 'white'
            mitreview.insert("", 0, values=(fila.producto, fila.stock, fila.preciocosto, fila.precioventa), tags =(my_tag))


    def modificar_producto(self, productid:str, stock:int, costo:float, precio:float, tree:Any, lista_entry:list) -> None:
        """
        Clear Screen, call modificar method of Model and show a message or update treeview depending of the case

        Args:
            producto (str, optional): Product id
            stock (str, optional): Current stock
            preciocosto (str, optional): Cost price
            precioventa (str, optional): Sell price
            tree (Any): Treeview object
            lista_entry (list): List with all Entries
        """
        self.clear_text(lista_entry)
        msg, frase = self.model.modificar(productid, stock, costo, precio)    
        if msg and frase:
            self.message(msg, frase)      
        else:
            self.actualizar_treeview(tree)


    def alta_producto(self, productid:str, stock:int, costo:float, precio:float, tree:Any, lista_entry:list) -> None:
        """
        Clear Screen, call alta method of Model and show a message or update treeview depending of the case

        Args:
            producto (str, optional): Product id
            stock (str, optional): Current stock
            preciocosto (str, optional): Cost price
            precioventa (str, optional): Sell price
            tree (Any): Treeview object
            lista_entry (list): List with all Entries
        """
        self.clear_text(lista_entry)
        msg, frase = self.model.alta(productid, stock, costo, precio)    
        if msg and frase:
            self.message(msg, frase)      
        else:
            self.actualizar_treeview(tree)

    def baja_producto(self, productid:str, tree:Any, lista_entry:list) -> None:
        """
        Clear Screen, call baja method of Model and show a message or update treeview depending of the case

        Args:
            producto (str, optional): Product id
            tree (Any): Treeview object
            lista_entry (list): List with all Entries
        """
        
        self.clear_text(lista_entry)
        msg, frase = self.model.baja(productid)
        if msg == "Error":
            self.message(msg, frase)

        if msg == "Delete Item":
            message = self.ask(msg, frase)
            if message == 'yes':
                self.model.borrar_sql(productid)
                self.actualizar_treeview(tree)


    def consultar_producto(self, productid:str, tree:Any, lista_entry:list) -> None:
        """
        Clear Screen, call consultar method of Model and show a message or update treeview depending of the case

        Args:
            producto (str, optional): Product id
            tree (Any): Treeview object
            lista_entry (list): List with all Entries
        """

        self.clear_text(lista_entry)
        self.actualizar_treeview(tree, productid)


    def vista_principal(self, root:Any) -> None:
        """
        App view building based on Tkinder library

        Args:
            root (Any): Tkinder object
        """
        utils = Utils()
        e_producto_id = StringVar()
        e_stock = IntVar()
        e_precio_costo = DoubleVar()
        e_precio_venta = DoubleVar()

        #Fijo el tamaño de la ventana y el título
        root.resizable(width=False, height=False)
        root.title('Control Stock Pañalera')

        #Seteo imagen de fondo
        try:
            image1 = Image.open("background.png")
            test = ImageTk.PhotoImage(image1)
            label1 = Label(image=test)
            label1.image = test
            label1.place(x=0, y=0)
        except Exception as e:
            error_reg.registrar_error(e)
            loggerService.error(e)
            

        menubar = Menu(root)
        root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        try:
            menubar.add_cascade(label="Archivo", menu=filemenu)
            filemenu.add_command(label="Exportar a csv", command=lambda:utils.savedbtocsv())
        except Exception as e:
            self.error.registrar_error(e)
            error_reg.registrar_error(e)

        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=root.quit)

        # Creo las etiquetas y los botones
        lab_producto_id = ttk.Label(root, text="Producto", background="pink")
        lab_stock = ttk.Label(root, text="Stock(u)", background="pink")
        lab_precio_costo = ttk.Label(root, text="Costo($)", background="pink")
        lab_precio_venta = ttk.Label(root, text="Precio($)", background="pink")

        e_producto_id = ttk.Entry(root, textvariable=lab_producto_id, width=21)
        e_stock = ttk.Entry(root, textvariable=lab_stock, width=13)
        e_precio_costo = ttk.Entry(root, textvariable=lab_precio_costo, width=13)
        e_precio_venta = ttk.Entry(root, textvariable=lab_precio_venta, width=13)
        lista_entry= [e_producto_id,e_stock,e_precio_costo,e_precio_venta]

  
        bot_buscar = ttk.Button(root, text='Buscar Producto', command=lambda:self.consultar_producto(
                                                                                    e_producto_id.get(),
                                                                                    tree,
                                                                                   lista_entry))
        
        bot_agregar = ttk.Button(root, text='Agregar Producto', command=lambda:self.alta_producto(
                                                                                    e_producto_id.get(),
                                                                                    e_stock.get(), 
                                                                                    e_precio_costo.get(),
                                                                                    e_precio_venta.get(),
                                                                                    tree,
                                                                                    lista_entry))
        bot_modificar = ttk.Button(root, text='Modificar Producto', command=lambda:self.modificar_producto(
                                                                                    e_producto_id.get(),
                                                                                    e_stock.get(), 
                                                                                    e_precio_costo.get(),
                                                                                    e_precio_venta.get(),
                                                                                    tree,
                                                                                    lista_entry))
        bot_eliminar = ttk.Button(root, text='Eliminar Producto', command=lambda:self.baja_producto(
                                                                                    e_producto_id.get(),
                                                                                    tree,
                                                                                    lista_entry))
        

        bot_salir = ttk.Button(root, text='Salir', command=root.quit)

        columns = ('product', 'stock', 'costo', 'precio venta')
        tree = ttk.Treeview(root, columns=columns, show='headings')
        tree.column("product", width=130, minwidth=130,anchor=CENTER)
        tree.column("stock", width=85, minwidth=85,anchor=CENTER)
        tree.column("costo", width=85, minwidth=85,anchor=CENTER)
        tree.column("precio venta", width=85, minwidth=85,anchor=CENTER)

        lab_producto_id.grid(column=2, row=0)
        lab_stock.grid(column=3, row=0)
        lab_precio_costo.grid(column=4, row=0)
        lab_precio_venta.grid(column=5, row=0)

        e_producto_id.grid(column=2, row=1)
        e_stock.grid(column=3, row=1)
        e_precio_costo.grid(column=4, row=1)
        e_precio_venta.grid(column=5, row=1)

        bot_buscar.grid(column=1, row=2)  
        bot_agregar.grid(column=1, row=3)
        tree.grid(column=2, row=2, columnspan=4, rowspan=4)
        bot_salir.grid(column=6, row=6)
        bot_eliminar.grid(column=1, row=5)
        bot_modificar.grid(column=1, row=4)


