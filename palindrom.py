name=['n','e','y','a','n']
i=0
list_n=[]
while i<len(name):
    a=name[-i-1]
    list_n.append(a)
    i=i+1
if list_n==name:
    print("it is palindrom")
else:
    print("it is not palindrom")
    
