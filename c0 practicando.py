c0=int(input("agrega el numero: "))
pasos=int(0)
while c0>0:
    if c0==1:
        break
    else:
        if c0%2==0:
            c0=c0//2
            print(c0)
        else:
            c0=3*c0+1
            print(c0)
    
    pasos+=1
print("pasos = ",pasos)

