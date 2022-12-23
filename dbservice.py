import re
import sqlite3
import tkinderservice


def conexion():
    con = sqlite3.connect("mibase.db")
    return con

def actualizar_tree(tree, product = ""):
        sql_all = "SELECT * FROM productos ORDER BY id ASC"
        if product:
            sql_all = f'SELECT * FROM productos  WHERE producto="{product}"'   
        con=conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql_all)
        resultado = datos.fetchall()
        tkinderservice.actualizar_treeview(tree, resultado)
        
            


def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    
    check_table = """SELECT count(name) FROM sqlite_master WHERE type='table' AND name='productos' """
    if not cursor.execute(check_table).fetchall()[0][0]:

        sql = """CREATE TABLE productos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 producto varchar(20) NOT NULL,
                 stock int(20),
                 preciocosto float(20),
                 precioventa float(20) )
        """
        cursor.execute(sql)
        con.commit()

def alta(producto='', stock='', preciocosto='', precioventa='', tree='', lista_entry =[]):
    tkinderservice.clear_text(lista_entry)
    con=conexion()
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
            actualizar_tree(tree)
        else:
            tkinderservice.message("Error","Productos: Solo letras y números\nStock: "+
                                    "Solo números\nPrecio: Usar '.' para decimales")
    else:
        tkinderservice.message("Error","Producto Ya existente")
        
    


def baja(producto="", tree='',lista_entry =[]):
    tkinderservice.clear_text(lista_entry)
    con=conexion()
    cursor=con.cursor()
    patron_prod="^[A-Za-záéíóú0-9]*$" #regex Se aceptan numeros y letras, sin caracteres especiales
    sql_all = f'SELECT * FROM productos  WHERE producto="{producto}"'  
    datos = cursor.execute(sql_all )
    if datos.fetchall():
        if(re.match(patron_prod, producto) and producto):
            msg_box = tkinderservice.ask('Delete Item', f'Are you sure you want to delete {producto} product?')
            if msg_box == 'yes':
                sql="DELETE FROM productos WHERE producto = ?; "
                data = (producto,) 
                cursor.execute(sql, data )
                con.commit()
                actualizar_tree(tree)        
        else:
            tkinderservice.message("Error","Productos: Solo letras y números en campo Producto\nCampo Producto obligatorio")
    else:
        tkinderservice.message("Error","Producto inexistente")

def consultar(producto="", tree='',lista_entry =[]):
    tkinderservice.clear_text(lista_entry)
    sql_all = f'SELECT * FROM productos  WHERE producto="{producto}"'
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql_all)   
    if producto:
        actualizar_tree(tree,producto)
    else:
        actualizar_tree(tree)
    return datos.fetchall()

def modificar(producto='', stock='', preciocosto='', precioventa='', tree='',lista_entry =[]):
    tkinderservice.clear_text(lista_entry)
    con=conexion()
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
            except:
                tkinderservice.message("Error","Producto inexistente")
            actualizar_tree(tree)
        else:
            tkinderservice.message("Error","Productos: Solo letras y números\nStock: "+
                            "Solo números\nPrecio: Usar '.' para decimales\nCampo Producto obligatorio")
    else:
        tkinderservice.message("Error","Por favor indicar que valor quiere modificar")
