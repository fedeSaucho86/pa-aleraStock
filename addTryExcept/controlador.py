from vista import Vista 
from tkinter import Tk
from model1 import Modelo
from loggerService import loggerService 
from error_register import ErrorRegister

class Controlador():
    def __init__(self) -> None:
        self.model = Modelo()
        

if __name__ == "__main__":
    root_tk = Tk()
    view = Vista(root_tk)
    root_tk.mainloop()