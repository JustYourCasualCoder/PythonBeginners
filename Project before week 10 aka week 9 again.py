y = 'y'
while y == 'y':
    b = int(input("How big do u want the triangle to be? "))
    for i in range (0,b):
        for j in range (0,i+1):
            print(">", end =" ")
        print()
    i=b
    while i > 0:
        j= 1
        while j <= i-1:
            print('<', end =" ")
            j = j+1 
            
        print()
        i = i-1

    y = input("enter y to keep going: ")
