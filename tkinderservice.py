from tkinter import *
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
    mitreview.tag_configure('grey', background='lightgrey')
    mitreview.tag_configure('white', background='white')
    for i, fila in enumerate(resultado):
        if i % 2 == 0:
            my_tag = 'grey' 
        else:
            my_tag = 'white'
        mitreview.insert("", 0, values=(fila[1], fila[2], fila[3], fila[4]), tags =(my_tag))

#Limpia los campos Entry
def clear_text(lista_entry):
    for entry in lista_entry:
        entry.delete(0, END)