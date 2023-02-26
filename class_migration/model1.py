import sqlite3
from peewee import *
import re

db = SqliteDatabase("mibase.db")


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = AutoField()
    producto =  CharField(unique=True),
    stock = IntegerField(),
    preciocosto = FloatField(),
    precioventa = FloatField()

    
db.connect()
db.create_tables([User])    
    
class Modelo():
    def __init__(self) -> None:
        pass
    
    
    
    
    """
    def crear_tabla(self, ):
        pass


    def alta(self, producto='', stock='', preciocosto='', precioventa=''):
        con= self.conexion()
        cursor=con.cursor()
        patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
        patron_stock=""
        patron_float_costo=""
        patron_float_venta=""

        if preciocosto:
            patron_float_costo="^[0-9]+([.][0-9]+)?$" #regex float
        if precioventa:
            patron_float_venta="^[0-9]+([.][0-9]+)?$" #regex float
        if stock:
            patron_stock= "^[0-9]*$" #regex numeros
        sql_all = f'SELECT * FROM productos  WHERE producto="{producto}"'  
        datos = cursor.execute(sql_all)
        if not datos.fetchall():
            if(re.match(patron_prod, producto) and re.match(patron_stock, stock) 
                and re.match(patron_float_costo, preciocosto) and re.match(patron_float_venta, precioventa)
                and producto):
                data = (producto, stock, preciocosto, precioventa)
                sql="INSERT INTO productos(producto, stock, preciocosto, precioventa) VALUES(?, ?, ?,?)"
                cursor.execute(sql, data)
                con.commit()
                return "",""
            else:
                return "Error","Productos: Solo letras y números\nStock: " \
                                        "Solo números\nPrecio: Usar '.' para decimales"
        else:
            return "Error","Producto Ya existente"


    def baja(self, producto=""):
        con=self.conexion()
        cursor=con.cursor()
        patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
        sql_all = f'SELECT * FROM productos  WHERE producto="{producto}"'  
        datos = cursor.execute(sql_all )
        if datos.fetchall():
            if(re.match(patron_prod, producto) and producto):
                return 'Delete Item', f'Are you sure you want to delete {producto} product?'                  
            else:
                return "Error","Productos: Solo letras y números en campo Producto\nCampo Producto obligatorio"
        else:
            return "Error","Producto inexistente"

    def borrar_sql(self, producto):
        con=self.conexion()
        cursor=con.cursor()            
        sql="DELETE FROM productos WHERE producto = ?; "
        data = (producto,) 
        cursor.execute(sql, data )
        con.commit()

    def consultar(self, producto=""):
        sql_all = f'SELECT * FROM productos  WHERE producto="{producto}"'
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql_all)   
        if producto:
            return "IS"
        else:
            return "IS NOT"

    def modificar(self, producto='', stock='', preciocosto='', precioventa=''):
        con=self.conexion()
        cursor=con.cursor()
        patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
        patron_stock=""
        patron_float_costo=""
        patron_float_venta=""
        sentence=""
        i = 0
        if preciocosto:
            patron_float_costo="^[0-9]+([.][0-9]+)?$" #regex float
            sentence = f" preciocosto = {preciocosto}" 
            i =+ 1
        if precioventa:
            patron_float_venta="^[0-9]+([.][0-9]+)?$" #regex float
            if i == 1:
                sentence = sentence + f", precioventa = {precioventa}"
            else: 
                sentence = sentence + f"precioventa = {precioventa}"
        if stock:
            patron_stock= "^[0-9]*$" #regex numeros
            if i >= 1:
                sentence = sentence + f", stock = {stock}"
            else:
                sentence = sentence + f"stock = {stock}"
        if sentence:    
            if(re.match(patron_prod, producto) and re.match(patron_stock, stock) 
            and re.match(patron_float_costo, preciocosto) and re.match(patron_float_venta, precioventa)
            and producto):
                try:
                    sql=f'UPDATE productos SET {sentence} where producto="{producto}";'
                    cursor.execute(sql)
                    con.commit()
                    return "", ""
                except:
                    return "Error", "Producto inexistente"
            else:
                return "Error", "Productos: Solo letras y números\nStock: " \
                                "Solo números\nPrecio: Usar '.' para decimales\nCampo Producto obligatorio"
        else:
            return "Error","Por favor indicar que valor quiere modificar"
        """
