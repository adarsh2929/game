score = 0 
def q1():
    global score
    print("q-1=what are two thingsyou can never eat for breakfast??")
    print("""
    
          [a]=snakes
          [b]=launch

          [c]=dinner
          [d]=lunch and dinner
                            """)
    choice=input("enter your choice")
    if choice=='d':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    print(score)
def q2():
    global score 
    print("q-2  what never ask a question but get answer all time ")
    print("""
    
    
        [a]=cow
        [b]=cell phone
        [c]=cealing fan
        [d]=donkey
                       """)
    choice=input("enter your choice")
    if choice=='b':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    
    print(score)

def q3():
    global score
    print("q-3 what goes up but never ever comes down")
    print("""
    
    
        a=airoplane
        b=roket launcher
        c=age
        d=spaceship
                       """)
    choice=input("enter your choice")
    if choice=='c':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q4():
    global score
    print("q-4 how can i go 20 days without sleep??")
    print("""
    
    
        [a]=with drink of tea
        [b]=i dont hav sleep
        [c]=i sleep in  night
        [d]=i just hate to sleep
                       """)
    choice=input("enter your choice")
    if choice=='c':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q5():
    global score
    print("q-5 what will u find after every rainbow")
    print("""
    
    
        [a]=rain
        [b]=clouds
        [c]=w
        [d]=birds in sky
                       """)
    choice=input("enter your choice")
    if choice=='c':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q6():
    global score
    print("q-6 i start out tall,but longer i stand the shorter i grow,what am i??")
    print("""
    
    
        [a]=watchmen
        [b]=zebra
        [c]=a candle
        [d]=elephant
                       """)
    choice=input("enter your choice")
    if choice=='c':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q7():
    global score
    print("q-7 what can run but not walk??")
    print("""
    
    
        [a]=leopard
        [b]=lion
        [c]=rain drop
        [d]=a cat
                       """)
    choice=input("enter your choice")
    if choice=='c':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q8():
    global score
    print("q-8 what is i know but dont tell u??")
    print("""
    
    
        [a]=mobile no
        [b]=atm pin
        [c]=secret
        [d]=idea
                       """)
    choice=input("enter your choice")
    if choice=='d':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q9():
    global score
    print("q-9 some months have 31 days some has 30 days but how many month have 28 days?")
    print("""
    
    
        [a]=march
        [b]=all of 12 month
        [c]=february
        [d]=august and december
                       """)
    choice=input("enter your choice")
    if choice=='b':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
def q10():
    global score
    print("q-10 imagine you r in a room which are filling up with water quikly.ther are no windows or doors,how do you get out")
    print("""
    
    
        [a]=by terrace
        [b]=by lifeguard jaket
        [c]=stop imagining
        [d]=by water pipe
                       """)
    choice=input("enter your choice")
    if choice=='c':
        #global score
        score=score+100
        print("correct ans")
    else:
        score=score-50
        print("incorrect ans")
    
    
    print(score)
q1()
q2()
q3()
q4()
q5()
q6()
q7()
q8()
q9()
q10()
print()
print("         |::::\\\\\\\\\\\\\\\\\\\\\\\\\\//////////////////////////::::|             ")
print(f"                   YOUR TOTAL SCORE IS : {score} ")   
print()

if score==0:
    print("         sorry better luck next time        ")

elif score < 0:
    print("        ***********||||  sorry you played very bad       ||||*************          ")
    print("        ***********||||  you have to pay 10000 rs  ||||*************          ")
elif score in range(100,201):
    print("        ***********||||  you have won 2000 rs      ||||**************         ")
elif score in range(201,501):
    print("        ***********||||  you have won 5000 rs      ||||**************         ")
elif score in range(501,701):
    print("        ***********||||  you have won 10000 rs      ||||**************         ")
elif score in range(701,1001):
    print("        ***********||||   you played exellent         ||||**************        ")
    print("        ***********||||  you have won 25000 rs      ||||**************        ")

