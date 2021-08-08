#  second max element
n = [50, 40, 89, 70, 56, 12, 78, 10, 7,87] 
i=0
a=n[0]
while i<len(n):
    if n[i]>a:
        a=n[i]
    i=i+1
n.remove(a)
b=0
k=n[0]
while b<len(n):
    if n[b]>k:
        k=n[b]
    b=b+1
print(k)
