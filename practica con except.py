def readint(prompt, min, max):
    try:
        prompt=int(input())
        if prompt<min or prompt>max:
            print("El valor no esta dentro del rango:", str(min),"hasta",str(max))
            return readint(print("Ingresa un numero de -10 a 10: " , end=''),-10,10)
    except ValueError:
        print("Error de entrada volver a intentar")
        return readint(print("Ingresa un numero de -10 a 10: " , end=''),-10,10)
    else:
        return prompt



v = readint(print("Ingresa un numero de -10 a 10: ", end=""),-10,10)

print("El numero es:", v)