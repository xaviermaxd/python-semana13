caracter = input("ingrese un caracter : ")


def vocal(x):
    return True if x in ["a","e","i","o","u"] else False


print(vocal(caracter))