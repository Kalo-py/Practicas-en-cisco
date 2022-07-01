def fun(linea):
    l=[]
    a=""
    for i in linea:
        if i==" ":
            l.append(a)
            a=" "
            continue
        else:
            a+=i
    if a!=" ":
        l.append(a)
    return l

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = fun(linea)
print(strings)
total=float(0)
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")
