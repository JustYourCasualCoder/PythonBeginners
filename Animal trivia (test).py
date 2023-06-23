
global sc
def check_guess(guess,ans):
    global sc
    sc=0
    life=3
    using = True
    while life >= 1 and using== True:
        if guess.lower() == ans.lower():
             print ("correct")
             sc +=1
             using = False
             return sc
        else:
            print ("incorrect")
            life -=1
            sc-=1
            guess = input ("try again ")
            if life == 0:
                print ("answer is", ans)
                

    
print("Welcome to animal trivia")
score = 0
G1 = input('which bear lives at the North pole? ')
score += check_guess (G1, 'polar bear')

G2 = input('are pandas rare? ')
score +=check_guess (G2, 'yes')

G3 = input('Where can you see animals that do not belong in your country? ')
score +=check_guess (G3, 'zoo')

G4 = input('are there lions in zoos? ')
score +=check_guess (G4, 'yes')

G5 = input('are plastics harmful to animals? ')
score +=check_guess (G5, 'yes')

print('Your score is',score)
