#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle 
#t1 for top message,t2 for word guess,t3 for attempts left,
#t4 for wrong guesses,t5 for drawing ambulance
#t6 for you lose
scr = turtle.Screen()
scr.title("Guess The Word Game !!")
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()
turtle.bgcolor("yellow")
flag=1
while(flag==1):
    t1.hideturtle()
    t1.up()
    t1.setx(-310)
    t1.sety(270)
    t1.down()
    #print(t1.position())
    t1.color("blue","blue")
    t1.write("Guess the word:",font=('Courier', 35, 'bold','italic'),align="left")

    t2.hideturtle()
    t2.color("blue","blue")
    t3.hideturtle()

    t4.hideturtle()
    t4.color("green","green")

    t5.hideturtle()
    t5.color("blue","white")
    t5.width(4)

    t6.hideturtle()
    t6.color("black")
    def erasableWritet2(text):
        t2.clear()
        t2.up()
        t2.setx(-310)
        t2.sety(225)
        t2.down()
        t2.write(text.lstrip(),font=('Courier', 35, 'bold','italic'),align="left")

    def erasableWritet3(turns):
        t3.clear()
        t3.up()
        t3.setx(0)
        t3.sety(-310)
        t3.down()
        t3.write("You have "+str(turns)+" attempts left",font=('Courier', 20,'italic'),align="center")

    def erasableWritet4(WrongGuesses):
        t4.clear()
        t4.up()
        t4.setx(-310)
        t4.sety(-230)
        t4.down()
        t4.write("Wrong Guesses:",font=('Courier', 35, 'bold','italic'),align="left")
        t4.up()
        t4.setx(-310)
        t4.sety(-270)
        t4.down()
        t4.write(WrongGuesses,font=('Courier', 35, 'bold','italic'),align="left")

    def draw():
        if(turns==7):
            t5.up()
            t5.setx(-100)
            t5.down()
            t5.begin_fill()
            for i in range(4):
                if i%2==0:
                    t5.forward(135) 
                else:
                    t5.forward(100)
                t5.right(90)
            t5.end_fill()
        elif(turns==6):
            t5.up()
            t5.setx(35)
            t5.sety(-30)
            t5.down()
            t5.begin_fill()
            for i in range(4):
                if i%2==0:
                    t5.forward(70)
                else:
                    if(i==3):
                        t5.width(0.5)
                    t5.forward(70)
                t5.right(90)
            t5.end_fill()   
        elif(turns==5):
            t5.up()
            t5.color("blue","blue")
            t5.setx(-50)
            t5.sety(-130)
            t5.begin_fill()
            t5.circle(30)
            t5.end_fill()
            t5.down()
        elif(turns==4):
            t5.up()
            t5.setx(50)
            t5.sety(-130)
            t5.begin_fill()
            t5.circle(30)
            t5.end_fill()
            t5.down()
        elif(turns==3):
            t5.up()
            t5.width(4)
            t5.setx(47)
            t5.sety(-39)
            t5.color("blue","white")
            t5.down()
            for i in range(4):
                if i%2==0:
                    t5.forward(40)
                else:
                    t5.forward(20)
                t5.right(90)
        elif(turns==2):
            t5.up()
            t5.width(4)
            t5.setx(-40)
            t5.sety(9)
            t5.color("blue","red")
            t5.down()
            t5.begin_fill()
            for i in range(4):
                if i%2==0:
                    t5.forward(15)
                else:
                    t5.forward(9)
                t5.right(90)
            t5.end_fill()
        elif(turns==1):
            t5.up()
            t5.width(4)
            t5.setx(-58)
            t5.sety(-26)
            t5.color("white","red")
            t5.begin_fill()
            for i in range(4):
                if i%2==0:
                    t5.forward(55)
                else:
                    t5.forward(20)
                t5.right(90)
            t5.end_fill()
            t5.down()
        elif(turns==0):
            t5.up()
            t5.width(4)
            t5.setx(-40)
            t5.sety(-9)
            t5.color("white","red")
            t5.begin_fill()
            for i in range(4):
                if i%2==0:
                    t5.forward(20)
                else:
                    t5.forward(55)
                t5.right(90)
            t5.end_fill()
            t5.down()
            t6.up()
            t6.setx(0)
            t6.sety(120)
            t6.down()
            t6.color("black","black")
            t6.write("YOU  LOSE !",font=('Courier', 50, 'bold'),align="center")

    print("----------PLAYER 1----------")
    print("")
    print("(Make sure player 2 is not peaking!)") 
    word = input("Enter your word (if it has a space use '-', e.g. ice-cream) : ") 
    for i in range(200):
        print("")
    print("---------PLAYER 2---------")
    print("")
    print("")

    guesses = '' 
    wrongGuesses = ""

    #any number of turns can be used here 
    turns = 8
    erasableWritet3(turns)
    guess=""
    while turns > 0: 

        # counts the number of times a user fails 
        failed = 0
        text=""
        # all characters from the input 
        # word taking one at a time. 
        for char in word: 

            # comparing that character with 
            # the character in guesses 
            if char in guesses: 
                text=text+"  "+char

            else: 
                text+="  *"

                # for every failure 1 will be 
                # incremented in failure 
                failed += 1
        erasableWritet2(text)
        if failed == 0: 
            # user will win the game if failure is 0 
            # and 'You Win' will be given as output 
            print("You Win") 

            # this print the correct word 
            print("The word is: ", word) 
            break

        # if user has input the wrong alphabet then 
        # it will ask user to enter another alphabet 
        print("")
        guess = input("guess a letter:") 

        # every input character will be stored in guesses 
        guesses += guess 

        # check input with the character in word 
        if guess not in word: 

            turns -= 1
            wrongGuesses=wrongGuesses+"  "+guess 
            erasableWritet4(wrongGuesses)
            erasableWritet3(turns)
            draw()
    for i in range(200):
        print("")
    x=input("Press any key to restart the game. ")
    t1.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t5.clear()
    t6.clear()
    for i in range(200):
        print("")


# In[ ]:




