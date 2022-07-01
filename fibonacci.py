def fib(n):
    if n==0:
        return None
    if n<3:
        return 1
    elem1=elem2=1
    suma=0
    for i in range(3,n+1):
        suma=elem1+elem2
        elem1,elem2=elem2,suma
    return suma


for n in range(10):
    print(n,"--->",fib(n))