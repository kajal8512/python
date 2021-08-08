# find the no. b/w 20 and 40.
n=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
i=0
list_l=[]
while i<len(n):
    num=n[i]
    if num<40 and num>20:
        print("number:",num)
        list_l.append(num)
    i=i+1
print(len(list_l))
