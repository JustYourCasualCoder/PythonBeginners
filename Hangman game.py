print("hang man game")
secWord = "paris"
print ("category: Location")

##letter_1 = input("input a letter: ")
##print("letter 1 in the secret world", letter_1 in secWord)
##letter_2 = input("input a letter: ")
##print("letter 2 in the secret world", letter_2 in secWord)
##letter_3 = input("input a letter")
##print("letter 3 in the secret world", letter_3 in secWord)
##letter_4 = input("input a letter")
##print("letter 4 in the secret world", letter_4 in secWord)
##letter_5 = input("input a letter")
##print("letter 5 in the secret world", letter_5 in secWord)
aw = 'y'
while aw == 'y':
        for i in range (0,6):
            letter = input("any letter: ")
            if letter.lower() in secWord:
                print("correct guess")
            else:
                print("incorrect letter") 


        fwg = input("guess for the full word: ")
        if fwg.lower() == secWord:
            print("correct guess")

        else:
            print("incorrect guess, try again")


        aw = input("enter y to continue: ")

