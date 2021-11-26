import datetime


def mostrarFecha():
    fechaActual = datetime.datetime.now()
    print("fecha actual: ",fechaActual.strftime("%d/%m/%y"))
    print("hora actual: ",fechaActual.strftime("%H:%M:%S"))


mostrarFecha()