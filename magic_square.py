m_s = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
i=0
while i<len(m_s):
    j=0
    s=0
    while j<len(m_s[i]):
        b=m_s[i][j]
        s=s+b
        j+=1
    i+=1
print(s)
# while 
# i=0
# s=0
# while i<len(m_s):
#     c=m_s[i]
#     # print(c)
#     s=s+c
#     i+=1