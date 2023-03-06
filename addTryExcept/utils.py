import csv
from model import Modelo
import time
from loggerService import loggerService 
from error_register import error_reg

timestr = time.strftime("%Y%m%d-%H%M%S")

class Utils():
     
     def __init__(self, ) -> None:
          """
          Instanciate Modelo to getting information from db
          """
          self.model = Modelo()
     
     def savedbtocsv(self, ) -> None:
          """
          Make query to database and export it to csv File
          """
          sql_query = self.model.consultar()
          try: 
               with open(f"export_{timestr}.csv", "w", newline='') as myfile:
                    csvwriter = csv.writer(myfile, delimiter=',')
                    for row in sql_query.tuples():
                        csvwriter.writerow(row)
          except Exception as e:
               error_reg.registrar_error(e)
               loggerService.error(e)

