import os
import datetime

class ErrorRegister(Exception):

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, f"log_{datetime.datetime.now().date()}.txt")

    def __init__(self,):
        pass

    def registrar_error(self, linea):
        log = open(self.ruta, "a")
        print(datetime.datetime.now(),": ", linea, file=log)

error_reg = ErrorRegister()

