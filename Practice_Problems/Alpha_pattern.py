def pattern(Lines):
    lines = Lines
    for  left in range(lines):
        start = 65
        for char1  in range(left,lines-1):
            print(chr(start),end = " ")
            start += 1
        for space1 in range(left):
            print(" "*2,end= "")
        for space2 in range(left):
            print(" "*2,end = "")
        for char2 in range(left,lines):
            print(chr(start),end = " ")
            start -= 1
        print()





Lines = int(input("Please enter the no of rows u want in the pattern: "))
pattern(Lines)
