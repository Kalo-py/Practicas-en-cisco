miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
repetido=[]
resultantList = []
for i in miLista:
    if i not in resultantList:
        resultantList.append(i)
    elif i in resultantList:
        if i not in repetido:
            repetido.append(i)
        

print(resultantList)
repetido.sort()
print("las repeticiones son: ", repetido)
