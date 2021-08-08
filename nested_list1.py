a=[1,2,[3,4],8,7,[5,6]]
k=[]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            k.append(a[i][j])
            j+=1
    else:
        k.append(a[i])
    i+=1
print(k)



