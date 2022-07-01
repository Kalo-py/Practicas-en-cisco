def a(pro,mini,maxi):
    try:
        mini=int(input("Numero menor:"))
        maxi=int(input("Numero mayor:"))
        pro=int(input("Numero medio: "))
        if pro>mini and pro<maxi:
            return pro
        else:
            print("Error: el valor no está dentro del rango permitido " + str(mini) + " hasta " + str(maxi))
            return a(print("Agrega un valor papu"),print("no te preocupes"),print("eres listo ;)"))
    except ValueError:
        print("no sirve")
        return a(print("Agrega un valor papu"),print("no te preocupes"),print("eres listo ;)"))
print("Programa para agregar numeros")
b=a(print("Agrega un valor papu",end=""),print("no te preocupes",end=""),print("eres listo ;)"))
print("El numero ingresado correctamente es: ",b)