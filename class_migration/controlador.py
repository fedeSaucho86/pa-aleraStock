from tkinter import Tk
from vista import Vista 
from modelo import Modelo

class Controlador():
    def __init__(self) -> None:
        self.model = Modelo()
  

if __name__ == "__main__":
    root_tk = Tk()
    view = Vista(root_tk)
    root_tk.mainloop()