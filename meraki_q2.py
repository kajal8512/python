# n=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# l=len(n)
# i=0
# l_t40=0
# m_t20=0
# while i<l:
#     nb=b[i]
#     if nb<40 and nb>20:
#         print()

A = [1,2,3,4,5,6]
B = [2,3,1,0,6,7]
i=0
k=[]
while i<len(A):
    a=A[i]
    if a not in B :
        k.append(a)
    i=i+1
print(k)
