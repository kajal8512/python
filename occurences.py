name=['k','a','j','a','l']
i=0
k=[]
while i<len(name):
    j=0
    c=0
    l=[]
    while j<len(name):
        if name[i]==name[j]:
            c+=1
        j+=1
    l.append(name[i])
    l.append(c)
    if l not in k:
        k.append(l)
    i+=1
print(k)

    

