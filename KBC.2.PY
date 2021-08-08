print("Welcome to K.B.C...\U0001F911..\U0001F911")
quest_l=["What is the capital of up?",
"Which is the largest temple in the Delhi?",
"who is the finance minister of India?"]

option_l=[["lukhnow","Gorakhpur","Kanpur","Delhi"],
["nilam mata","lotus","yogmaya temple","Akshardham temple"],
["Narendra Modi","Kejarival","Nirmala Sitharaman","Uddhav Thackeray"]]

solution_l=[1,4,3]

life_l=[["1.Delhi","2.lukhnow"],
["1.nilam mata","2.Akshardham"],
["1.Nirmala Sitharaman","2.Narendra Modi"]]

life_sol=[2,2,1]

que=0   # for questions 
while que<len(quest_l):
    print(quest_l[que])
    optn=0  #for options
    while optn<len(option_l[que]):
        print(optn+1,".",option_l[que][optn])
        optn+=1
    que+=1
    sol=0
    life_line=input("Do you want lifeline..")
    if life_line=="yes":
        print(life_l[0])
        Answer=int(input("Enter your answer.."))
        if Answer==life_sol[0]:
            print("correct")
    
    

        
    