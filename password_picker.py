import string
import random



adjectives = ['sleepy', 'slow', 'smelly','wet', 'fat', 'red',
'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon',
'hammer', 'duck', 'panda']


#print ("Adjectives: ",adjectives, "\n","nouns: ", nouns)
print ("welcome to password picker")
Using = 'yes'
while Using.lower() == 'yes':
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    number = str(random.randrange(0,99))
    spacial_char= random.choice(string.punctuation)
    print("generated password: ")
    print(noun + adjective + spacial_char + number)
    Using = input("Enter yes to generate new password: ")
    if Using.lower() == 'no':
        print("Thank you for using the service")
