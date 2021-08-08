list=[1,2,3,4,5,6,7,8,9]
k=[]
i=1
user=int(input("enter the no."))
while user<len(list):
    a=list[-user-1]
    k.append(a)
    user+=1
print(k)
    
