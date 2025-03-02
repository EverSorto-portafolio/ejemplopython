import math

# def es una funcion que recibe dos parametros, precio e interes, y retorna el resultado de multiplicar precio por interes
# precio: int
# interes: int
# float: int
def calcularInteres(precio, interes):

    return precio * interes

def calcularPrecio(precio, ganacia):

    return precio + (ganacia * precio)


def  precioVenta(precio, interes, ganacia):
    total = calcularPrecio(precio, ganacia)
    interes = calcularInteres(total, interes)
    return  total + interes
 
interes = float(input("Ingrese el interes: "))
precio = float(input("Ingrese el precio: "))    
ganacia = float(input("Ingrese la ganacia: "))

print(precioVenta(precio, interes, ganacia))