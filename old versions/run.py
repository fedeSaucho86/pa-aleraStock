from tkinter import *
from tkinter import ttk
import utils
import dbservice

##############Inicialización DB################################################
try:
    con = dbservice.conexion()
    dbservice.crear_tabla()
except Exception as e:
    print("No se ha podido crear la tabla: ", e)


###############Creación TKINDER#######################################################
root = Tk()

#Definición de variables
producto_id = StringVar()
stock = IntVar()
precio_costo = DoubleVar()
precio_venta = DoubleVar()

#Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title('Control Stock Pañalera')

#Seteo imagen de fondo
imagen = PhotoImage(file = "background.png")
background = Label(root, image = imagen).place(x=0,y=0)

#Creo Menu bar
menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Exportar a csv", command=lambda:utils.savedbtocsv())
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

bot_buscar = ttk.Button(root, text='Buscar Producto', command=lambda:dbservice.consultar(
                                                                            e_producto_id.get(),
                                                                            tree,
                                                                            lista_entry))

bot_agregar = ttk.Button(root, text='Agregar Producto', command=lambda:dbservice.alta(
                                                                            e_producto_id.get(),
                                                                            e_stock.get(), 
                                                                            e_precio_costo.get(),
                                                                            e_precio_venta.get(),
                                                                            tree,
                                                                            lista_entry))

bot_modificar = ttk.Button(root, text='Modificar Producto', command=lambda:dbservice.modificar(
                                                                            e_producto_id.get(),
                                                                            e_stock.get(), 
                                                                            e_precio_costo.get(),
                                                                            e_precio_venta.get(),
                                                                            tree,
                                                                            lista_entry))

bot_eliminar = ttk.Button(root, text='Eliminar Producto', command=lambda:dbservice.baja(
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
bot_modificar.grid(column=1, row=4)
bot_eliminar.grid(column=1, row=5)
tree.grid(column=2, row=2, columnspan=4, rowspan=4)
bot_salir.grid(column=6, row=6)


mainloop()