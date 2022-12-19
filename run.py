from tkinter import *
from tkinter import ttk
import sqlite3
import re
from tkinter import messagebox as MessageBox
import dbservice


##############Inicializate DB################################################
try:
    con = dbservice.conexion()
    dbservice.crear_tabla()
except Exception as e:
    print("No se ha podido crear la tabla: ", e)


###############Creation TKINDER#######################################################
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

# Creo las etiquetas y los botones
lab_producto_id = ttk.Label(root, text="Producto")
lab_stock = ttk.Label(root, text="Stock")
lab_precio_costo = ttk.Label(root, text="Costo")
lab_precio_venta = ttk.Label(root, text="Precio")

e_producto_id = ttk.Entry(root, textvariable=lab_producto_id, width=15)
e_stock = ttk.Entry(root, textvariable=lab_stock, width=15)
e_precio_costo = ttk.Entry(root, textvariable=lab_precio_costo, width=15)
e_precio_venta = ttk.Entry(root, textvariable=lab_precio_venta, width=15)

bot_buscar = ttk.Button(root, text='Buscar Producto', command=lambda:dbservice.consultar(
                                                                            e_producto_id.get(),
                                                                            tree))
bot_agregar = ttk.Button(root, text='Agregar Producto', command=lambda:dbservice.alta(
                                                                            e_producto_id.get(),
                                                                            e_stock.get(), 
                                                                            e_precio_costo.get(),
                                                                            e_precio_venta.get(),
                                                                            tree))
bot_modificar = ttk.Button(root, text='Modificar Producto', command=lambda:dbservice.modificar(
                                                                            e_producto_id.get(),
                                                                            e_stock.get(), 
                                                                            e_precio_costo.get(),
                                                                            e_precio_venta.get(),
                                                                            tree))
bot_eliminar = ttk.Button(root, text='Eliminar Producto', command=lambda:dbservice.baja(
                                                                            e_producto_id.get(),
                                                                            tree))
bot_salir = ttk.Button(root, text='Salir', command=root.quit)

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3","col4")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80)
tree.column("col2", width=80, minwidth=80)
tree.column("col3", width=80, minwidth=80)
tree.column("col4", width=80, minwidth=80)

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