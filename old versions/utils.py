import csv
import dbservice
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

def savedbtocsv():
     con = dbservice.conexion()
     c=con.cursor()
     mysel=c.execute("select * from productos ")
     with open(f"export_{timestr}.csv", "w", newline='') as myfile:
          csvwriter = csv.writer(myfile, delimiter=',')
          for row in mysel:
              csvwriter.writerow(row)

