#La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
#Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
#La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal - 
# si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de la palabra clave except 
# debería proporcionar una reacción adecuada a la excepción planteada.
#Se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")
print("FIN.")


try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
#Si se ingresa 0, dirá:
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
#Si se ingresa cualquier cadena no entera, verás
except ValueError:
    print("Debes ingresar un valor entero.")
#si presionas Ctrl-C mientras el programa está esperando la entrada del usuario el programa dirá
except:
    print("Oh cielos, algo salio mal...")
#Si se ingresa un valor entero válido distinto de cero (por ejemplo, 5) dirá
print("THE END.")