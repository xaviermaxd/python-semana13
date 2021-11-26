lista = []
x = int(input("cantidad de terminos de una lista: "))
for i in range(x):
    n = int(input("ingrese un numero: "))
    lista.append(n)
print(lista)

def sumar(numeros):
    return sum(numeros)


def multiplicar(numeros):
    mul = 1
    for i in numeros:
        mul *= i
    return mul


print("la suma es: ",sumar(lista))
print("la multiplicacion es :",multiplicar(lista))