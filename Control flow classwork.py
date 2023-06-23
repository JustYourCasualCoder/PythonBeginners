##cake = input("Do you like cake? (yes/no)")
##
##if cake == 'Y' or 'y' or 'Yes' or 'YES' or 'ye'
##print("Yay! Me too.")
##
##
##energy_level = input("Are you tired? (yes/no) ")
##if energy_level == "yes" or "y" or "YES":
##    print("You better get some sleep")
##
##
##elif energy_level == 'no' or 'NO' or 'N' or 'n':
##    print("lets play something")
##
##
##
##fav_pet = input("What's your favorite pet? (dog/cat/parrot) ")
##if fav_pet == 'dog' or fav_pet =='Dog':
##    print("Dogs are friendly")
##
##elif fav_pet == 'cat' or fav_pet == 'Cat':
##    print ("cats are quiet")
##
##elif fav_pet == 'parrot':
##  print("parrots are colourfull")
##
##else:
##    print("invailed")
##
##
##number = int(input("input any number: "))
##if number < 0:
##    print("Negative number")
##
##elif number > 0:
##    print("Postive number")
##
##elif number == 0:
##    print("number is zero")
##
##else:
##    print("invalided input")

aw = 'y'
while aw == 'y':

        Std_Nm = input("Student name: ")

        age = int(input("Student age: "))
                    
        mk_1 = float(input("input mark for subject 1: "))
                     
        mk_2 = float(input("input mark for subject 2: "))
                    
        mk_3 = float(input("input mark for subject 3: "))
                     
        mk_4 = float(input("input mark for subject 4: "))
                     
        mk_5 = float(input("input mark for subject 5: "))

        ag = (mk_1 + mk_2 + mk_3 + mk_4 + mk_5)/5
        print("Name: ", Std_Nm)
        print("age:", age)
        print("average is %0.2f " %(ag)) 


        if ag >=90 and ag <=100:
            print("Grade A")
            
        elif ag >=75 and ag <=89:
            print("Grade B")

        elif ag >=60 and ag <= 74:
            print("Grade C")

        elif ag >=50 and ag <=59:
            print("Grade D")
            
        elif ag >=0 and ag <=49:
            print("Fail")

        else:
            print("invailed output. Double check the marks")

        aw = input("enter y to continue: ")
else:
        print("Thank you for using the service")


