import math

x = float(input("Ingresa un numero: "))
#Si la expresión se evalúa como True (verdadero), o un valor numérico distinto de cero, o una cadena no vacía, o cualquier otro valor diferente de None, no hará nada más.
assert x != None

x = math.sqrt(x)

print(x)

#Puedes ponerlo en la parte del código donde quieras estar absolutamente a salvo de datos incorrectos, 
# y donde no estés absolutamente seguro de que los datos hayan sido examinados cuidadosamente antes (por ejemplo, dentro de una función utilizada por otra persona).
#Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.
