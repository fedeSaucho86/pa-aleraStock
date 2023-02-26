import sqlite3
from peewee import *
import re
from loggerService import loggerService 
from error_register import error_reg

try:
    db = SqliteDatabase("mibase.db")
except Exception as e:
    error_reg.registrar_error(e)
    loggerService.error(e)



class BaseModel(Model):
    class Meta:
        database = db

class Inventory(BaseModel):
    id = AutoField()
    producto =  CharField(unique=True)
    stock = IntegerField()
    preciocosto = FloatField()
    precioventa = FloatField()

    
db.connect()
db.create_tables([Inventory])    
    
class Modelo():
    def __init__(self) -> None:
        pass


    def alta(self, producto='', stock='', preciocosto='', precioventa=''):
        inventory = Inventory()
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
        query = Inventory.select().where(Inventory.producto == producto)
        if not len(query):
            if(re.match(patron_prod, producto) and re.match(patron_stock, stock) 
                and re.match(patron_float_costo, preciocosto) and re.match(patron_float_venta, precioventa)
                and producto):
                inventory.producto = producto
                inventory.stock = stock
                inventory.preciocosto = preciocosto
                inventory.precioventa = precioventa
                inventory.save()

                return "",""
            else:
                return "Error","Productos: Solo letras y números\nStock: " \
                                        "Solo números\nPrecio: Usar '.' para decimales"
        else:
            return "Error","Producto Ya existente"

     
    def consultar(self, producto=""):
        if producto:
            query = Inventory.select().where(Inventory.producto == producto)
            return query
        else:
            return Inventory.select()
    
    def baja(self, producto=""):
        patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
        query = Inventory.select().where(Inventory.producto == producto)  
        if len(query):
            if(re.match(patron_prod, producto) and producto):
                return 'Delete Item', f'Are you sure you want to delete {producto} product?'                  
            else:
                return "Error","Productos: Solo letras y números en campo Producto\nCampo Producto obligatorio"
        else:
            return "Error","Producto inexistente"

    def borrar_sql(self, producto):       
        #sql="DELETE FROM productos WHERE producto = ?; "
        query = Inventory.delete().where(Inventory.producto == producto)
        query.execute()
        pass
        

    def modificar(self, producto='', stock='', preciocosto='', precioventa=''):
        patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
        patron_stock=""
        patron_float_costo=""
        patron_float_venta=""
        query = Inventory.select().where(Inventory.producto == producto) 
        for valor in query:
            if not preciocosto:
                preciocosto = str(valor.preciocosto)
            else:
                patron_float_costo="^[0-9]+([.][0-9]+)?$"
            if not precioventa:
                precioventa = str(valor.precioventa)
            else:
                patron_float_venta="^[0-9]+([.][0-9]+)?$" 
            if not stock:
                stock = str(valor.stock)
            else:
                patron_stock= "^[0-9]*$"      

        if producto:  
            if(re.match(patron_prod, producto) and re.match(patron_stock, stock) 
            and re.match(patron_float_costo, preciocosto) and re.match(patron_float_venta, precioventa)
            and producto):
                if len(query):
                    actualizar=Inventory.update(producto = producto, stock = stock, precioventa = precioventa, preciocosto = preciocosto).where(Inventory.producto == producto)
                    actualizar.execute()
                    return "", ""
                else:
                    return "Error", "Producto inexistente"
            else:
                return "Error", "Productos: Solo letras y números\nStock: " \
                                "Solo números\nPrecio: Usar '.' para decimales\nCampo Producto obligatorio"
        else:
            return "Error","Por favor indicar que producto quiere modificar"
