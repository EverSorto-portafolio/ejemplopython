# uso simple 
simple = "Soy un texto simple"

#texto multilinea
textoGrande = ''' Tengo muchas lineas 
                muuchas lineas 
 '''
#Concatenar (Unir text0)
unir = simple + textoGrande
#multplicar texto|
unir = simple * 2
print(unir)

print(" lineas  1 \n linea 2 \n linea 3")
print(" tabulador \t tabulador")
print(" retroceso \b retroceso")
print(" comilla simple \' comilla simple")
print(" comilla doble \" comilla doble")
print(" barra invertida \\ barra invertida")
print(" salto de pagina \f salto de pagina")
print(" retorno de carro \r retorno de carro")
print(" salto de linea \n salto de linea")

texto = "dasdfasdfasdfasdfqweqwerqwdasdfasdf"
print(len(texto))
texto[0]
texto[1]
print(texto[1:10])
print(texto[:10])
print(texto[-10])
print(texto[-10::2])
for letra in texto:
    print(letra)