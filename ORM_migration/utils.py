import csv
from model1 import Modelo
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

class Utils():
     
     def __init__(self, ) -> None: 
          self.model = Modelo()
     
     def savedbtocsv(self, ):
          sql_query = self.model.consultar()
          with open(f"export_{timestr}.csv", "w", newline='') as myfile:
               csvwriter = csv.writer(myfile, delimiter=',')
               for row in sql_query.tuples():
                   csvwriter.writerow(row)

