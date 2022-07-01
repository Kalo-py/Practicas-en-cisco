from datetime import datetime
s1 = input("agrega algo vida:")
s2 = input("agrega algo vida:")
format = '%H:%M:%S'
time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
print(time)