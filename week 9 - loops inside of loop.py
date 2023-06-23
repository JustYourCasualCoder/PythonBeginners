##for i in range (1,5):
##    for j in range (1,i+1):
##        print('*', end =" ")
##    print("\n")
##
##nm = input("input your name: ")
##print('Hello,%s!' %(nm))
##
##nm = input("input your name: ")
##ag = int(input("input age: "))
##print("%s is %d years old." %(nm,ag))
##
##for i in range (1,5):
##    for j in range (i):
##        print(i,end =" ")
##    print()
##
##for i in "Welcome to Ultimate Coders":
##    if i == 'a' or i == '





##
##
##for i in range (0,4):
##    for j in range (0,i+1):
##        print('*', end =" ")
##    print()



##
##
##b = int(input("How big do u want the triangle to be? "))
##for i in range (0,b):
##    for j in range (0,i+1):
##        print('*', end =" ")
##    print()

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
              


