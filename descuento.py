#- si la compra es mayor a
#    - 50 → 0.05
#    - 100 → 0.10
#    - 200 → 0.12
#    - 1000 → 0.2
#- Mostrar
#- total real
#- total descuento
#- total a pagar

compra = float(input("Ingrese el monto de compra "))
descuento = 0

def mostrar(compra, descuento):
    
    if compra < 50 : 
        print("Total sin descuento " , compra)
        print("Descuento :  no aplica")  
        print("Total a pagar " , compra)
    else:
        descuento = compra * descuento
        total = compra - descuento 
        print("Total sin descuento " , compra)
        print("Descuento :  " , descuento)  
        print("Total a pagar " , total)

if compra >= 50  and compra < 100:
    descuento = 0.05

if compra >= 100  and compra < 100:
    descuento = 0.10

if compra >= 100  and compra < 200:
    descuento = 0.12

if compra >= 200  and compra < 1000:
    descuento = 0.2
mostrar(compra, descuento)