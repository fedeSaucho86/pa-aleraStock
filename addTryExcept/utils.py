import csv
from model1 import Modelo
import time
from loggerService import loggerService 
from error_register import error_reg

timestr = time.strftime("%Y%m%d-%H%M%S")

class Utils():
     
     def __init__(self, ) -> None: 
          self.model = Modelo()
     
     def savedbtocsv(self, ):
          sql_query = self.model.consultar()
          try: 
               with open(f"export_{timestr}.csv", "w", newline='') as myfile:
                    csvwriter = csv.writer(myfile, delimiter=',')
                    for row in sql_query.tuples():
                        csvwriter.writerow(row)
          except Exception as e:
               error_reg.registrar_error(e)
               loggerService.error(e)

