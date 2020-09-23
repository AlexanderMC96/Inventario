class Producto:
    def __init__(self,id_articulo,articulo,tipo_articulo,precio,stock):
        self.id_articulo = id_articulo
        self.tipo_articulo=tipo_articulo
        self.articulo = articulo
        self.tipo_articulo=tipo_articulo
        self.precio=precio
        self.stock = stock
    
    # Con la funcion repr, la salida de los datos seran en string, si no hacemos esto
    # Serian del tipo hexadecimal 
    def __repr__(self):
        return "Producto({},'{}','{}',{},{})".format(self.id_articulo,self.articulo,self.tipo_articulo,
        self.precio,self.stock)
    
    

        