import csv
from modelo import Modelo
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

class Utils():
     
     def __init__(self, ) -> None: 
          self.model = Modelo()
     
     def savedbtocsv(self, ):
          con = self.model.conexion()
          c=con.cursor()
          mysel=c.execute("select * from productos ")
          with open(f"export_{timestr}.csv", "w", newline='') as myfile:
               csvwriter = csv.writer(myfile, delimiter=',')
               for row in mysel:
                   csvwriter.writerow(row)

