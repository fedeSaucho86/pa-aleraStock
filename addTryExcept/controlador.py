from vista import Vista 
from tkinter import Tk

class Controlador():
    def __init__(self) -> None:
        pass
        
if __name__ == "__main__":
    root_tk = Tk()
    view = Vista(root_tk)
    root_tk.mainloop()