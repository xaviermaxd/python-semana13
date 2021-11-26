import datetime
from datetime import timedelta

año1 = int(input('Introduzca el año de la primera fecha: '))
mes1 = int(input('Introduzca el mes de la primera fecha: '))
dia1 = int(input('Introduzca el dia de la primera fecha: '))

fecha1 = datetime.date(año1, mes1, dia1)
print("primer fecha es: ",fecha1)
print(" "*30)

año2 = int(input('Introduzca el año de la segunda fecha: '))
mes2 = int(input('Introduzca el mes de la segunda fecha: '))
dia2 = int(input('Introduzca el dia de la segunda fecha: '))

fecha2 = datetime.date(año2, mes2, dia2)
print("segunda fecha es: ",fecha2)
print(" "*30)


def dias(x,y):
    return(x-y).days


print("la deiferencia de dias es: ",dias(fecha1,fecha2))