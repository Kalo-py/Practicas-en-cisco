def control(pal1,pal2):
    pal1=pal1.lower()
    pal2=pal2.lower()
    if sorted(pal1)==sorted(pal2):
        return "Son anagramas"
    else:
        return "No lo son"




pal1=str(input("Ingresa la primera palabra papu: "))
pal2=str(input("Ingresa la segunda palabra papu: "))
print(control(pal1,pal2))
