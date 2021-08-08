marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
] 

i=0
sum=0
av=0
length=len(marks)
while i<length:  
    s=0
    k=0
    while k<len(marks[i]):
        s=s+(marks[i][k])
        k=k+1
    sum=sum+s
    av=sum/length
    i=i+1
print(av)

            


        
