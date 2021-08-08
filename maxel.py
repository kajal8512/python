# find max element
n = [50, 40, 89, 70, 56, 12, 78, 10, 7,100] 
i=0
a=n[0]
while i<len(n):
    if n[i]>a:
        a=n[i]
    i=i+1
print(a)
