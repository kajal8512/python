# n_l = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# a=n_l[0]
# l=[]
# while i<len(n_l):
#     if n_l[i]>a:
#         a=n_l[i]
#         l.append(a)
#     elif n_l[i]<a:
#             i=i+1
# print(a)

# n_l = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# i=0
# a=1
# m=max(n_l[i],n_l[a])
# s_mx=min(n_l[i],n_l[a])
# n=len(n_l)
# for i in range(2,n):
#     if n_l[i]>m:
#         s_mx=m
#         mx=n_l[i]
#     elif n_l[i]>s_mx and m!=n_l[i]:
#         s_mx=n_l[i]
#         i+=1
#         a+=1
# print("second max no.",str(s_mx))