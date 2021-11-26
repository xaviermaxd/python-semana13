from datetime import datetime, timedelta

formato = "%d/%m/%Y"
contador = 0            
fechaInicio = input('Fecha desde (dd/mm/aaaa): ')
fechaFinal = input('Fecha hasta (dd/mm/aaaa): ')

                 
fechaInicio = datetime.strptime(fechaInicio, formato)
fechaFinal = datetime.strptime(fechaFinal, formato)    


while fechaInicio < fechaFinal:
    if datetime.weekday(fechaInicio) == 6: 
        contador +=1
        fechaactual = fechaInicio.strftime(formato)
        print(fechaactual, 'es domingo')
    fechaInicio = fechaInicio + timedelta(days=1)
print("son ",contador," domingos en total")
