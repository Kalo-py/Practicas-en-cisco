import datetime
hora_actual=datetime.datetime.now()
print("hora actual: ", hora_actual)
resultado=hora_actual + datetime.timedelta(minutes=59)
print("la hora mas 59 minutos es: ", resultado)