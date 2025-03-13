
#Evaluar varias condiciones 
# if, elif, else
# if ->si 
# else -> sino
# elif -> sino si
# and -> y
# or -> o
# not -> no
# == -> igual
# != -> diferente
# < -> menor que
# > -> mayor que
# <= -> menor o igual que
# >= -> mayor
# True -> verd
# False -> falso
 
valor = int(input("Ingrese un valor: "))
valor2 = int(input("Ingrese un valor: "))

if valor> valor2:
    print(" es mayor ")
else:
    print("no es mayor que ")



def par(valor):
    resultado = "Es par" if valor % 2 == 0 else "Es impar"
    return resultado

def positivoOnegativo(valor):
    resultado = "negativo" if valor<0 else "positivo"
    return resultado

def detectarLetras(valor):
    if any(c.isalpha() for c in str(valor)):
        return True
    else:
        return False

def parYsigno( func1, func2 ):
    if func1(valor) ==  "negativo" and func2(valor) =="Es impar":
        return "negativo,impar"
    if func1(valor) ==  "positivo" and func2(valor) =="Es impar":
        return "positivo, impar"
    if func1(valor) ==  "positivo" and func2(valor) =="Es par":
        return "positivo, par"
    if func1(valor) ==  "positivo" and func2(valor) =="Es impar":
        return "positivo, impar"


45
if not detectarLetras(valor):
    resultado = parYsigno(positivoOnegativo,par)
    print(f'El numero {valor} es {resultado}')
else:
    print("Solo numeros")



