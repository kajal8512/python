print("Welcome to K.B.C...\U0001F911..\U0001F911")
quest_l=["What is the capital of up?",
"Which is the largest temple in the Delhi?",
"who is the finance minister of India?"]

option_l=[["1.Delhi","2.Gorakhpur","3.Kanpur","4.lukhnow"],
["1.nilam mata","2.lotus","3.yogmaya temple","4.Akshardham temple"],
["1.Nirmala Sitharaman","2.Narendra Modi","3.Kejarival","4.Uddhav Thackeray"]]

solution_l=[4,4,1]

life_l=[["1.Delhi","2.lakhnow"],
["1.nilam mata","2.Akshardham"],
["1.Nirmala Sitharaman","2.Narendra Modi"]]
i=0 
a=0 #for option_l 
while i<len(quest_l):
    print(quest_l[i]) 
    b=0 
    while b<len(option_l[a]):
        print(option_l[a][b])
        b=b+1
    a=a+1
    j=0
    user=int(input("enter your answer"))
    while j<len(solution_l):
        if user==solution_l[j]:
            print("congrats! your answer is correct")
        else:
            print("your answer is wrong")
        j+=1
        break
        
    i+=1
    # l=input("Do you want life line")
    # if l=="yes":
    #     print("ok..\U0001F920")
    #     ans1=input("enter your answer")
    #     if ans1==solution_l[0]:
    #         print("congrats! your answer is correct")
    
        
        






    




    # user=input("enter your answer1")
    # if user==solution_l[0]:
    #     print("your answer is correct")
    #     user1=input("enter your answer2")
    #     if user1==solution_l[1]:
    #         print("your answer is correct")
    #         user3=input("enter the answer3")
    #         if user3==solution_l[2]:
    #             print("you answer is correct")
        
     





















