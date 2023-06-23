###One branch
##is_dark = input ("is it dark outside? (y/n):" " ")
##
###Condition
##if is_dark == 'y' or is_dark == 'Y' or is_dark == 'YES' or is_dark == 'Yes':
##    print("Goodnight! Zzzzz...")
##
##elif: is_dark == "n" or is_dark == "N" or is_dark == "NO" or is_dark == "No":
##    ("good day")
##
##
##else:
##    print("invalided")

#multiple branches
Temp = int(input("What is the Temperature today?" " "))

if Temp >= -5 and Temp <= 5: 
    print("Moderate")

elif Temp >= +5 and Temp <= 30:
    print("sunny")

elif Temp >= +30:
    print("hot day")

elif Temp >= -30 and -5:
    print("cold")

else: Temp <= -30
print("extreme cold")

