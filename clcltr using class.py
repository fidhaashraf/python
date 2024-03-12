class Calculator:
    def addition(self):
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        sum=a+b
        print(sum)
    def substraction(self):
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        sub = a-b
        print(sub)
    def multiplication(self):
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        mult = a*b
        print(mult)
    def division(self):
        a=int(input("enter a number"))
        b=int(input("enter a number"))
        division = a/b
        print(division)
c=Calculator()
while True:
    print("1.addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    choice = int(input("enter your choice:"))
    if choice==1:
        c.addition()
    elif choice==2:
        c.substraction()
    elif choice==3:
        c.multiplication()
    elif choice==4:
        c.division()

