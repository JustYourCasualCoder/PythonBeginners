def neg_zero_pos (a):
    if a > 0:
        print ("number is positive")

    elif a == 0:
        print ("number is zero")

    elif a<0:
        print ("negative number")

    else:
        print  ('error')

a = int(input("what number: "))

neg_zero_pos (a)
