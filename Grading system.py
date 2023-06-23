
Using = 'yes'

while Using == 'yes':
    Nm = input("Student name: ")
    Rn = input("roll number: ")
    s = 0
    for i in range(5):
        tp = int(input( "Grade: "))
        s += tp
        
    avg = s/5
    print (avg)

    if 85 < avg <=100:
        print("A")
    elif 75 < avg <= 85:
        print('B')
    elif 65 < avg <= 75:
        print('C')
    elif 50 < avg <= 65:
        print('D')

    elif 0 <= avg <= 50:
        print("F")

    else:
        print("invalid input")


    Using = input ("Enter yes if you want to continue using our services: ")

