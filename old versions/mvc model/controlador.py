from tkinter import Tk
import vista 
from class_migration.modelo import conexion, crear_tabla

if __name__ == "__main__":
    try:
        con = conexion()
        crear_tabla()
    except Exception as e:
        print("No se ha podido crear la tabla: ", e)
    root_tk = Tk()
    vista.vista_principal(root_tk)
    root_tk.mainloop()