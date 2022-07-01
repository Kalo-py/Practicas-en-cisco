def misplit(strng):
    split_val = []
    temp = ''
    for c in strng:
        if c == ' ':
            split_val.append(temp)
            temp = ''
        else:
            temp += c
    if temp:
        split_val.append(temp)
    return split_val
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))