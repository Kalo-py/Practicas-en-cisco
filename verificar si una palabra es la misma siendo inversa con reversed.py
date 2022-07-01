palabra1=input("ingresa la palabra que quieras: ")
palabra1=palabra1.replace(" ","")
palabra1=palabra1.lower()
if str(palabra1) == "".join(reversed(palabra1)) :
    print("Palindrome")
else:
   print("Not Palindrome")