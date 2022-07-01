dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)
#el popitem elimina el ultimo elemento del diccionario
dict.popitem()
print(dict)