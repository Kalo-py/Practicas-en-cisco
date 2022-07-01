# Ejemplo 1: Demostración del método islower()
#El método islower() es una variante de isalpha() - solo acepta letras minúsculas.
print("El método islower() es una variante de isalpha() - solo acepta letras minúsculas.")
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
#El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro caracter (el resultado es entonces False).
print("\n El método isspace() identifica espacios en blanco solamente - no tiene en cuenta ningún otro caracter (el resultado es entonces False).")
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper() 
#El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.
print("\n El método isupper() es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.")
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())