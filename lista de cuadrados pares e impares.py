cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)
impar= [x for x in cuadrados if x % 2 != 0] 
print(impar)
par = [x for x in cuadrados if x % 2 == 0] 
print(par)