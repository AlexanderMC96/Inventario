# Trabajamos con Programacion ORIENTADA a Objetos
import sqlite3
import os
from producto import Producto

DB_NAME = "./Clase11-db-python/db-poo/FerreteriaCOCO2.db"
# Crear el objeto de conexion en este caso le ponemos conn por convencion
conn = sqlite3.connect(DB_NAME)
# Crear el cursor para la conexion. 
c = conn.cursor()

# Creando la tabla
def create_table():
    c.execute("""CREATE TABLE producto(
                    id_articulo INTEGER PRIMARY KEY,
                    articulo TEXT,
                    tipo_articulo TEXT,
                    precio REAL,
                    stock INTEGER)
                """)
def menu():

    print('Hola, bienvenido al Inventario de "Ferreteria COCO\n\n')
    print('A continuacion se le presenta el menú de opciones...')
    
    print('\n **************** MENÚ ****************\n')
    
    print('1) Visualizar tabla de productos')
    print('2) Crear e insertar productos')
    print('3) Actualizar stock')
    print('4) Eliminar productos')
    print('0) Salir')
    
    print()

def insertar_producto(prod):
    # With es una sentencia que permite garantizar que
    #una determinada instruccion se cumpla.
    # Funciona como try y except. Con una determinada conexion
    # 'conn' va a ejecutar una instruccion que le pasemos
    with conn:
        c.execute("INSERT INTO producto VALUES(:id_producto,:nombre_producto,:tipo_producto,:precio_producto,:stock_producto)",
        {'id_producto':prod.id_articulo,'nombre_producto':prod.articulo,'tipo_producto':prod.tipo_articulo,'precio_producto':prod.precio,'stock_producto':prod.stock}                    
        )
                    
                    
def obtener_producto_por_tipo(tipo_articulo):
    c.execute("SELECT * FROM producto WHERE tipo_articulo =:tipo_producto",{'tipo_producto':tipo_articulo})
    return c.fetchall()

def ver_producto_unico(id_articulo):
    c.execute("SELECT * FROM producto WHERE id_articulo=:id_producto",
    {'id_producto':id_articulo})
    return c.fetchone()
            
def ver_productos():
    c.execute("SELECT * FROM producto")
    return c.fetchall()
def actualizar_stock(id_prod,stock_prod):
    # Utilizar el with solo en caso de que se haga una modificacion sensible es decir 
    # que sea estricta (INSERTAR, ACTUALIZAR, ELIMINAR). No se utiliza en casos de solo visualizar la data
    
    with conn:
        id_prod = int(input('Ingrese el número identificador de producto: '))
        stock_prod= int(input('Ingrese el nuevo stock del producto: '))
        new_data=(id_prod,stock_prod)
        c.execute(""" UPDATE producto SET stock = ?  WHERE id_articulo =? """,
                    (id_prod,stock_prod)
        )
              
    
def eliminar_producto(prod):
    #Nunca olvidar usar la instruccion WHERE  para la funcion DELETE, se echaria a perder todo
    with conn:
        c.execute("""DELETE FROM producto WHERE id_articulo= :id_producto""",
                    {'id_producto':prod.id_articulo}
                )

def cleaning():
    while True:
        clean = str(input('Desea limpiar la pantalla (Y/N): '))
        if clean == 'Y':
            os.system('cls')
            break
        elif clean =='N':
            print("Vale...")
            break
        else:
            print('Error: Valor no válido')


if __name__ == '__main__':
    #create_table()
    
    # CREAMOS LA BASE DE DATOS DE UN INVENTARIO DE PRODUCTOS 

    while True:
        while True:
            menu()
            try:
               opcion = int(input("Digite la opción de menú: "))
               break
            except ValueError:
                print('ERROR: Vuelva a ingresar una opcion válida')
        
        if opcion == 0:
            break                                     
        if opcion >= 1 and opcion <=4:
            print('\nEspere un momento: \n...\n...\n...\n')
        if opcion == 1:
            print('¿Que consulta deseas hacer?: \n')
            print('1) Visualizar toda la tabla')
            print('2) Visualizar por Tipo de producto')  
            print()
            
            while True:
                opcion = int(input("Digite la opción de consulta: "))
                print()
                try:
                    if opcion ==1:
                        total_productos = ver_productos()
                        for i in total_productos:
                            print (i)
                        cleaning()
                        break
                    elif opcion ==2:
                        tipo = obtener_producto_por_tipo(input('Ingrese el tipo de producto que desea ver: '))
                        for i in tipo:
                            print (i)
                        cleaning()
                        break
                        
                except ValueError:
                    print('ERROR: Vuelva a ingresar una opcion válida')
                

        elif opcion ==2:
            while True:
                try:
                    id_prod = int(input('Ingrese un número identificador de producto:'))
                    nombre_prod = str(input('Ingrese el nombre del producto: '))
                    tipo_prod = str(input('Ingrese el tipo de producto: '))
                    precio_prod = float(input('Ingrese el precio del producto: '))
                    stock_prod= int(input('Ingrese el stock del producto: '))

                    prod_new=Producto(id_prod,nombre_prod,tipo_prod,precio_prod,stock_prod)
                    insertar_producto(prod_new)
                    break
                except ValueError:
                    print('ERROR: Vuelva a ingresar un dato válido.')
                             

        elif opcion ==3:
            print("IMPORTANTE: Es sumamente necesario escribir correctamente el ID del producto a modificar.\n")
            #while True:
            #    try:
                    #id_prod = int(input('Ingrese el número identificador de producto: '))
                    #stock_prod= int(input('Ingrese el nuevo stock del producto: '))
                            
            #        prod_unico=(ver_producto_unico(id_prod))
            #        print(prod_unico)

            #actualizar_stock(id_prod,stock_prod)
            #        print('Se ha actualizado correctamente.')
            cleaning()
            #        break
            #    except ValueError:
            #        print('ERROR: Vuelva a ingresar un dato válido.')

            #OJO: Si ingreso este tipo de dato, la funcion actualizar funciona con normalidad.
            # pro10 = Producto(10,'Wincha','Construccion',5,5)
            #print(type(pro10))
            #print(type(stock_prod))
            #      
        elif opcion ==4:
            print("IMPORTANTE: Es sumamente necesario escribir correctamente el ID del producto a eliminar.\n")
            while True:
                try:
                    id_prod = int(input('Ingrese el número identificador de producto: '))
                                              
                    prod_unico=(ver_producto_unico(id_prod))
                    print(prod_unico)

                    #eliminar_producto(prod_unico)
                    print('Se ha eliminado correctamente.')
                    cleaning()
                    break
                except ValueError:
                    print('ERROR: Vuelva a ingresar un dato válido.')
    
    print('Gracias por usar nuestro inventario... !!!')
                                  
    conn.commit()
    conn.close()        

            

            
            
        
        
    

