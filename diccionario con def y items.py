def traduccion(dict):
    for spanish, french in sorted(dict.items()):
        print(spanish, "->", french)



dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

traduccion(dict)
