
def control(birth):
    sum1=int(0)
    sum2=int(0)
    for i in birth:
        sum1+=int(i)
    print(sum1)
    birth=str(sum1)
    for j in birth:
        sum2+=int(j)
    return sum2





birth=str(input("Ingresa los valores: "))
print(control(birth))