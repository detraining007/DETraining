def Alphabets(line):
    ends = 70
    for alphabets in range(line):
        start = 65
        ends2 = ends
        for left_alpha in range(alphabets,line):
            print(chr(start),end=" ")
            start += 1
        for down_left in range(alphabets):
            print(" "*2,end = "")
        for down_right in range(alphabets):
            print(" "*2,end="")
        for right_alpha in range(alphabets,line):
            print(chr(ends2),end = " ")
            ends2 -=1
        ends -= 1
        print()







if __name__ == "__main__":
    lines = int(input("Enter the no of lines: "))
    print(Alphabets(lines))

