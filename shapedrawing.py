    import turtle
    s=turtle.getscreen()
    t = turtle.Turtle()
    turtle.bgcolor("white")
    t.fillcolor("black")
    t.shape("turtle")
    print('Press 1 for square. Press 2 for circle. Press 3 for triangle . Press 4 for rectangle')
    notdone = True
    while notdone:
        choice=input('1:/2:/3:/4:')
        t.home()
        t.clear()
        if choice =='1':
            t.clear()
            side=input("enter side length")
            side=int(side)
            t.fd(side)   
            t.rt(90)
            t.fd(side)
            t.rt(90)
            t.fd(side)
            t.rt(90)
            t.fd(side)
            t.home()
        elif choice =='2':
            t.clear()
            radius=input("enter radius")
            radius=int(radius)
            t.circle(radius)
            t.home()
        elif choice =='3':
            side1=input("enter side length")
            side1=int(side1)
            t.clear()
            t.fd(side1)
            t.lt(120)
            t.fd(side1)
            t.lt(120)
            t.fd(side1)
            t.home()
        elif choice =='4':
            t.clear()
            side1=input("enter side length")
            side1=int(side1)
            side2=input("enter side length")
            side2=int(side2)
            t.lt(90)    
            t.fd(side1)
            t.rt(90)
            t.fd(side2)
            t.rt(90)
            t.fd(side1)
            t.rt(90)
            t.fd(side2)
            t.home()
        else:
            print("invalid response.")
            contnue = input("Do you want to continue? (y/n) ")
            if contnue == "n":
                print("Thanks for using this code")
                notdone = False
                

    
    