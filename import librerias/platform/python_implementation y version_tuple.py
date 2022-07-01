from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr,"")

#Si necesitas saber qué versión de Python está ejecutando tu código, puedes verificarlo utilizando una serie de funciones dedicadas