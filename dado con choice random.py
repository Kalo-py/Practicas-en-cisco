from random import choice, sample

lst = [1, 2, 3, 4, 5, 6]

numeroaleatorio=choice(lst)
if numeroaleatorio%2==0:
    print(numeroaleatorio)
    print("ir a comer pizza")
else:
    print(numeroaleatorio)
    print("ir a comer hamburguesa")