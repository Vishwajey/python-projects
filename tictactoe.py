# This method will draw an X in the given location
def x(l):
    t.rt(45)
    t.fd(l/2)
    t.bk(l/2)
    t.lt(90)
    t.fd(l/2)
    t.bk(l/2)
    t.lt(90)
    t.fd(l/2)
    t.bk(l/2)
    t.lt(90)
    t.fd(l/2)
    t.bk(l/2)
    t.rt(225)
 
#This methodl asks the choice for Player 1 and draws a dot if the cell is unoccupied
def player1():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9

    turn="not complete"
    #Ask choice from Player 1 until a cell that is unoccupied is chosen
    while turn=="not complete":
        choice=input('Player 1: 1:/2:/3:/4:5:/6:/7:/8:/9:')
        if choice=='1':
            if c1 == 0:
                t.penup()
                t.goto(50,250)
                t.pendown()
                t.dot(75)
                c1=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='2':
            if c2 == 0:
                t.penup()
                t.goto(150,250)
                t.pendown()
                t.dot(75)
                c2=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='3':
            if c3 == 0:
                t.penup()
                t.goto(250,250)
                t.pendown()
                t.dot(75)
                c3=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='4':
            if c4 == 0:
                t.penup()
                t.goto(50,150)
                t.pendown()
                t.dot(75)
                c4=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice =='5':
            if c5 == 0:
                t.penup()
                t.goto(150,150)
                t.pendown()
                t.dot(75)
                c5=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='6':
            if c6 == 0:
                t.penup()
                t.goto(250,150)
                t.pendown()
                t.dot(75)
                c6=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='7':
            if c7 == 0:
                t.penup()
                t.goto(50,50)
                t.pendown()
                t.dot(75)
                c7=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='8':
            if c8 == 0:
                t.penup()
                t.goto(150,50)
                t.pendown()
                t.dot(75)
                c8=1
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='9':
            if c9 == 0:
                t.penup()
                t.goto(250,50)
                t.pendown()
                t.dot(75)
                c9=1
                turn="complete"
        else:
            print('this cell is taken')
            

def player2():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    turn="not complete"
    while turn=="not complete":
        choice=input('Player 2: 1:/2:/3:/4:5:/6:/7:/8:/9:')
        if choice=='1':
            if c1 == 0:
                t.penup()
                t.goto(50,250)
                t.pendown()
                x(75)
                c1=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='2':
            if c2 == 0:
                t.penup()
                t.goto(150,250)
                t.pendown()
                x(75)
                c2=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='3':
            if c3 == 0:
                t.penup()
                t.goto(250,250)
                t.pendown()
                x(75)
                c3=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='4':
            if c4 == 0:
                t.penup()
                t.goto(50,150)
                t.pendown()
                x(75)
                c4=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice =='5':
            if c5 == 0:
                t.penup()
                t.goto(150,150)
                t.pendown()
                x(75)
                c5=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='6':
            if c6 == 0:
                t.penup()
                t.goto(250,150)
                t.pendown()
                x(75)
                c6=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='7':
            if c7 == 0:
                t.penup()
                t.goto(50,50)
                t.pendown()
                x(75)
                c7=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='8':
            if c8 == 0:
                t.penup()
                t.goto(150,50)
                t.pendown()
                x(75)
                c8=2
                turn="complete"
            else:
                print('this cell is taken')
        elif choice=='9':
            if c9 == 0:
                t.penup()
                t.goto(250,50)
                t.pendown()
                x(75)
                c9=2
                turn="complete"
            else:
                print('this cell is taken')    
            

notdone = True
while notdone:
    #Create a new turtle object and draw a Tic Tac Toe grid on a blank screen
    import turtle
    s=turtle.getscreen()
    s.clear()
    s.reset()
    t = turtle.Turtle()
    t.reset()
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(0,200)
    t.pendown() 
    t.forward(300) 
    t.penup()
    t.goto(100,0)
    t.pendown()
    t.left(90)
    t.forward(300) 
    t.penup()
    t.goto(200,0)
    t.pendown()
    t.forward(300)
    #set 0 to all cell variables
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0
    c7=0
    c8=0
    c9=0

    #
    for i in range(0,5):
        player1()
        if (c1==1 and c2==1 and c3==1) or (c4==1 and c5==1 and c6==1) or (c7==1 and c8==1 and c9==1) or (c1==1 and c4==1 and c7==1) or (c2==1 and c5==1 and c8==1) or (c3==1 and c6==1 and c9==1) or (c1==1 and c5==1 and c9==1) or (c3==1 and c7==1 and c5==1):
            print("player 1 wins!")
            break
        player2()
        if (c1==2 and c2==2 and c3==2) or (c4==2 and c5==2 and c6==2) or (c7==2 and c8==2 and c9==2) or (c1==2 and c4==2 and c7==2) or (c2==2 and c5==2 and c8==2) or (c3==2 and c6==2 and c9==2) or (c1==2 and c5==2 and c9==2) or (c3==2 and c7==2 and c5==2):
            print("player 2 wins!")
            break
    contnue = input("Do you want to play again? (y/n) ")
    if contnue == "n":
        input("Game over! Press ENTER to close:")
        notdone=False
    else:
        notdone=True