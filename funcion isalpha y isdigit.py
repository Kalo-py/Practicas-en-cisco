# Ejemplo 1: Demostración del método isapha()
#El método isalpha() es más especializado, se interesa en letras solamente.
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit()
# Al contrario, el método isdigit() busca sólo dígitos - cualquier otra cosa produce False (falso) como resultado.
print('2018'.isdigit())
print("Año2019".isdigit())