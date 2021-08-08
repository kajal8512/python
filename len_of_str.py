string_l=["acb","4123","jkl","098"]
i=0
a=string_l[0]
count=0
while i<=len(string_l):
    if a<(len(string_l[i])):
        a=string_l[i]
        count=count+1
    i=i+1
print(a)
