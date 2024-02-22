count=1
rows=int(input("enter the no.of rows:"))
for i in range(1,rows):
    for j in range(i):
        print(count,end=" ")
        count+=1
    print()

