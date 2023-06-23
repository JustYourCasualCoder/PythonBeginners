#Functions

def add():
    x = int(input("number 1: "))
    y = int(input("number 2: "))
    z=x+y
    print(x,'+',y,'=',z)

def sub():
    x = int(input("number 1: "))
    y = int(input("number 2: "))
    z=x-y
    print(x,'-',y,'=',z)

def mui():
    x = int(input("number 1: "))
    y = int(input("number 2: "))
    z=x*y
    print(x,'x',y,'=',z)
    
def div():
    x = int(input("number 1: "))
    y = int(input("number 2: "))
    z =x/y 
    print(x,'/',y,'=',z)
    
#Main Code
y = 'y'
while y:
    print("welcome to python calculator")
    oi = input("what operation? ")

    if oi == 'add' or 'addition':
        add()

    elif oi == 'sub' or 'subtract':
        Sub()

    elif oi == 'times' or 'multiply':
        mui()

    elif oi == 'div':
        div()
    

    y = input ("Enter y if you want to continue using our services: ")
