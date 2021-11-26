import time


def mostrarHora():
    time12 = time.strftime("%I:%M:%S")
    time24 = time.strftime("%H:%M:%S")
    print("hora actual formato 12h es : ",time12)
    print("hora actual formato 24h es : ",time24)


def mostrarFecha():
    fecha = time.strftime("%d/%m/%y")
    print("fecha actual formato dia/mes/año es : ",fecha)
    

mostrarHora()
mostrarFecha()