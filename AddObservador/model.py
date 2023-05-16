from peewee import Model, AutoField, CharField, IntegerField, FloatField, SqliteDatabase
import re
from loggerService import loggerService 
from error_register import error_reg
from typing import Tuple, Any
from observador import Sujeto


try:
    db = SqliteDatabase("mibase.db")
except Exception as e:
    error_reg.registrar_error(e)
    loggerService.error(e)

def baja_producto(funcion):
    def envoltura(*args): 
        ret = funcion(*args)     
        print ("El producto que usted borró es: ", args[1])
        return ret
    return envoltura

def alta_producto(funcion):
    def envoltura(*args): 
        ret = funcion(*args)     
        print ("El producto que usted dió de alta es:", args[1], \
               " Stock:", args[2], " Precio costo:", args[3], \
                " Precio venta:" , args[4])
        return ret
    return envoltura


def modificar_producto(funcion):
    def envoltura(*args): 
        ret = funcion(*args)     
        print ("El producto que usted modifico es:", args[1], \
               " Stock:", args[2], " Precio costo:", args[3], \
                " Precio venta:" , args[4])
        return ret
    return envoltura

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
    
class Modelo(Sujeto):
    def __init__(self) -> None:
        pass

    @alta_producto
    def alta(self, producto:str='', stock:int = '', preciocosto:float = '', precioventa:float = '') -> Tuple[str,str]:
        """
        Register new product to inventory

        Args:
            producto (str, optional): Product id
            stock (str, optional): Current stock
            preciocosto (str, optional): Cost price
            precioventa (str, optional): Sell price

        Returns:
            Tuple[str,str]: Differents messages depending on choosen option
        """
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
                self.notificar("add", inventory.producto, inventory.precioventa)
                inventory.save()
                

                return "",""
            else:
                return "Error","Productos: Solo letras y números\nStock: " \
                                        "Solo números\nPrecio: Usar '.' para decimales"
        else:
            return "Error","Producto Ya existente"


    def consultar(self, producto:str = "")  -> Any :
        """
        Query to database to show it in Treeview App

        Args:
            producto (str, optional): Product Id

        Returns:
            Any: Return Query object -> All products or specific One
        """
        if producto:
            query = Inventory.select().where(Inventory.producto == producto)
            return query
        else:
            return Inventory.select()
    
    def baja(self, producto:str = "") -> Tuple[str,str]:
        """
        If product is not null and match with patterns, will be deleted in other method.

        Args:
            producto (str, optional): Product Id

        Returns:
            Tuple[str,str]: Differents messages depending on choosen option
        """
        patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
        query = Inventory.select().where(Inventory.producto == producto)  
        if len(query):
            if(re.match(patron_prod, producto) and producto):
                return 'Delete Item', f'Are you sure you want to delete {producto} product?'                  
            else:
                return "Error","Productos: Solo letras y números en campo Producto\nCampo Producto obligatorio"
        else:
            return "Error","Producto inexistente"
        
    @baja_producto
    def borrar_sql(self, producto:str = "") -> None:
        """
        To delete entries in DB after previous validations

        Args:
            producto (str, optional): Product Id
        """
        #sql="DELETE FROM productos WHERE producto = ?; "
        query = Inventory.delete().where(Inventory.producto == producto)
        self.notificar("delete", Inventory.producto)
        query.execute()
        pass
        
    @modificar_producto
    def modificar(self, producto:str='', stock:int = '', preciocosto:float = '', precioventa:float = '') -> Tuple[str,str]:
        """
        Modify Product/entries in Database

        Args:
            producto (str, optional): Product id
            stock (str, optional): Current stock
            preciocosto (str, optional): Cost price
            precioventa (str, optional): Sell price

        Returns:
            Tuple[str,str]: Differents messages depending on choosen option
        """
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
                    self.notificar("update", producto, precioventa)
                    actualizar.execute()
                    return "", ""
                else:
                    return "Error", "Producto inexistente"
            else:
                return "Error", "Productos: Solo letras y números\nStock: " \
                                "Solo números\nPrecio: Usar '.' para decimales\nCampo Producto obligatorio"
        else:
            return "Error","Por favor indicar que producto quiere modificar"
