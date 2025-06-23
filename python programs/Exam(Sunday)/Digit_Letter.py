def digit_letter(number):
    while number >0:
        number = int(number % 10)
        if number ==0:
            print("zero",end=" ")
        elif number ==1:
            print("one",end=" ")
        elif number ==2:
            print("Two",end=" ")
        elif number ==3:
            print("Three",end=" ")
        elif number ==4:
            print("Four",end=" ")
        elif number ==5:
            print("Five",end=" ")
        elif number ==6:
            print("six",end=" ")
        elif number ==7:
            print("Seven",end=" ")
        elif number ==8:
            print("Eight",end=" ")
        elif number ==9:
            print("Nine",end=" ")
        number = number/10
number = int(input("Enter number"))
digit_letter(number)