hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
time1=(dura+min)%60
time2=((min+dura)/60)+hora
time3=time2%24
print(time3,":",time1)
