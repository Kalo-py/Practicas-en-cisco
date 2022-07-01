print("\n\"Estableciendo los rangos para mas optimizacion desde el 1 al 11\"")
i=0
pow=2
for i in range(1,11):
    print("2 a la potencia de ", i,"es: ",pow)
    pow*=2

print("\n\"Reinicio del ciclo utilizando continue cuando pasa por el 0\"")
i=0
pow=1
for i in range(11):
    if i==0:
        pow*=2
        continue
    print("2 a la potencia de ", i,"es: ",pow)
    pow*=2

print("\n\"Reinicio del ciclo utilizando la condicion distinto a 0\"")
i=0
pow=2
for i in range(11):
    if i!=0:
        print("2 a la potencia de ", i,"es: ",pow)
        pow*=2
