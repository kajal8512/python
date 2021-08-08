'''b_n = [1, 0, 0, 1,1,1,1,1,1,0 ] 
i=0
sum=0
while i<len(b_n):
    b=(b_n[-i-1])*(2**i)
    sum=sum+b 
    # dec=sum%10
    c=sum/10  
    i=i+1
print("dec:",c)'''

'''if 5>4 and 5<6:
elif 6>4 and 5<6:
elif 4<6 and 4<5:
    print("it is greater ttan")
else:
    print("it is less than")'''

num1=int(input("enter any no."))
num2=int(input("enter any no."))
num3=int(input("enter the no."))
if num1<num2 or num2>num3:
    if num1<num3 or num2<num3:
        if num1>num2 or num1>num3:
            print("it is greater then")
        else:
            pass
    else:
        pass
else:
    print("it is smoller then")
    

