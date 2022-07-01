# El método replace() con dos parámetros devuelve una copia de la cadena original 
# en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


#La variante del métdodo replace() con tres parámetros emplea un tercer argumento (un número) para limitar el número de reemplazos.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))