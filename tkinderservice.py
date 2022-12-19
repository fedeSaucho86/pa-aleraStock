from tkinter import *
from tkinter import ttk

from tkinter import messagebox as MessageBox

def message(msg,frase = ""):
    MessageBox.showinfo(msg, frase)

def ask(msg,frase = ""):
    return MessageBox.askquestion(msg, frase, icon='warning')

def actualizar_treeview(mitreview, resultado):
    
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

