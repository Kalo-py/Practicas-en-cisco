def eli(list):
    for i in range(len(list)):
        if list[i]=="adriana albarn":
            list[i]="Crecimiento"
    return list

def vs(mami,toxica):
    for i in range(len(toxica)):
        if toxica[i]=="adictas":
            toxica[i],toxica[i+1]=toxica[i+1],toxica[i]
            del(toxica[-1])
            break
    print("viva cristo rey", mami)
    return toxica



cercanos=["brhyan","ale","markis","adri","adriana albarn"]
familiares=["jenny","liz","mami","papa","gerardo"]
toxica=["locas","feministas","adictas","abusadoras"]

for i in range(len(familiares)):
    if familiares[i]=="mami":
        mami=familiares[i]
        print(vs(mami,toxica))



print(familiares)
print(eli(cercanos))