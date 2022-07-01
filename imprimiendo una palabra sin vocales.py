p=str(input("Ingrese una palabra papirriki: "))
p=p.upper()


for letra in p:
    if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        continue
    print(letra)
