while True:
    print("1.caluclate perimeter of the circle")
    print("2.caluclate perimeter of the rectangle")
    print("3.caluclate perimeter of the square")
    print("4.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        radius=int(input("enter the randius"))
        perimeter=2*3.14*radius
        print(perimeter)
    elif choice==2:
        length=int(input("enter the length"))
        breadth=int(input("enter the breadth"))
        perimeter=2*length+width
        print(perimeter)
    elif choice==3:
        side=int(input("enter the side"))
        perimeter=4*side
        print(perimeter)
    elif choice==4:
        print("exit")
        break


