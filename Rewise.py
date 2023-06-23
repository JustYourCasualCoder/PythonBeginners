##Nm = input("name: ")
##Ag = int(input("age: "))
##Sch = input("School Name: ")
##print (Nm, "\n", Ag,"\n", Sch)



##
##    y = "yes"
##
##    while y == 'yes':
##        tmp = int(input("Temperature: "))
##
##        if tmp >= 1:
##            print("Spring is here")
##
##        elif tmp <= -1:
##            print("winter is here")
##
##        else:
##            print ("Freezing temperature")
##
##        y = input("Do you want to try it again? ")

    



Nm = input("name: ")
Ct = int(input("Phone number: "))
Ct2 = input("Email: ")

pr = 0

print ("Welcome")

P = input ("Phone or laptop? " )
if P.lower() == 'phone':
    print ("How much storage? \n 64Gb, 126Gb, 256Gb, 512Gb")
    st = int(input("Amount of storage: "))
    cnt = 64
    pr = 300
    for i in range(4): 
        if cnt == st:
            print("good choice,", cnt, "Gb")
            print("Price: ", pr)
            break
        cnt=cnt+cnt
        pr=pr+pr

    c = input("colour option: Black or Red?")
    if c.lower() == 'black':
        pr=pr+100
        print(pr)

    elif c.lower() == 'red':
        pr=pr+50
        print(pr)
    
    



if P.lower() == 'laptop':
    print ("How much storage? \n 256Gb,512,1tb")
    st = int(input("Amount of storage: "))
    cnt = 256
    pr = 600
    for i in range(4): 
        if cnt == st:
            print("good choice,", cnt, "Gb")
            print("Price: ", pr)
            break
        cnt=cnt+cnt
        pr=pr+pr

    
    print ("How much Ram? \n 16Gb,32Gb,64Gb")
    st = int(input("Amount of Ram: "))
    cnt = 16
    pr = 700
    for i in range(3): 
        if cnt == st:
            print("good choice,", cnt, "Gb")
            print("Price: ", pr)
            break
        cnt=cnt+cnt
        pr=pr+pr


        
