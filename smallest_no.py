'''number=[2,4,6,7,9,1]
i=0
a=number[0]
while i<len(number):
    if number[i]<a:
        a=number[i]
    i+=1
print(a)'''


'''my_file2 = open("people2.txt", "w")
my_file2.write("Abhishek - Gurgaon")
my_file2.write("Ranveer - Delhi")
my_file2.close()'''

my_file3 = open("people3.txt", "w")
my_file3.write("Abhishek - Gurgaon\n")
my_file3.write("Ranveer - Delhi")
my_file3.close() 