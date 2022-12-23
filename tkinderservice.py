from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox

#Mensaje acerca del formato de los parámetros de entrada
def message(msg,frase = ""):
    MessageBox.showinfo(msg, frase)

#Pregunta si estás seguro
def ask(msg,frase = ""):
    return MessageBox.askquestion(msg, frase, icon='warning')

#Muestra los resultados en la app
def actualizar_treeview(mitreview, resultado):
    
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    for fila in resultado:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

#Limpia los campos Entry
def clear_text(lista_entry):
    for entry in lista_entry:
        entry.delete(0, END)