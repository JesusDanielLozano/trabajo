class producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, provedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.provedor = provedor

productos= []

def mostrar_menu():

    print('MENU')
    print('1 ingreso el producto')
    print('2 producto de stock')
    print('3 buscar por  porvedores')
    print('4 buscar los productos')
    print('5 ver total de articulos')
    print('6 salir')

def investigar_producto():
    codigo = input('ingrese el codigo del producto')
    nombre = input('ingrese el nombre del producto')
    valor_compra = float(input('ingrese el valor de la compra del producto'))
    valor_venta = float(input('ingrese el valor de venta del prpducto'))
    stock_nimimo = int(input('ingrese el stock minimo pernitid'))
    stock_maximo = int(input('ingrese el stock maximo permitido'))
    provedor = input('ingrese el nombre del provedor del producto')

    producto = producto(codigo, nombre, valor_compra, valor_venta, stock_nimimo, stock_maximo, provedor)
    productos.append(producto)
    print('producto registrado exitosamente')
    

