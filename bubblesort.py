n=[5,6,7,4,3,2,1,8,9,10]
j=0
while j<len(n):
    i=0
    while i<len(n)-1:
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
        i+=1
    j+=1        
print(n)

# list=[2,9,4,5,6]
# print(list[1-1])
