list= [1, 1, 3, 4, 5, 6, 7]
list1=[0, 1, 2, 3, 4, 5, 7]
list2=[0, 1, 2, 3, 4, 5, 7]
i=0
k=[]
while i<len(list):
    a=list[i]=list1[i]=list2[i]
    k.append(a)
    i+=1
print(k)
