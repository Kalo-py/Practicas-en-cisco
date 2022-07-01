beatles=[]
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("\nPaso 2:", beatles)

for i in range(2):
    nom=str(input("Agregue al nuevo integrante: "))
    beatles.append(nom)
print("\nPaso 3:", beatles)

print("\nEliminando a los ultimos integrantes:", beatles[3:], " Adios")
del(beatles[3:])
print("\nPaso 4:", beatles)

print("\nAgregando a la bitch ")
beatles.insert(0,"Ringo Starr")
print("\nPaso 5:", beatles)



print("Los Fab", len(beatles))