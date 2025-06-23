def prime_leftPyramid(number):
    num = 2
    for row in range(number):
        print(" "*(number-(row+1)),end="")
        count =0
        while count <= row:
            flag = True
            for col in range(2,num):
                if num%col==0:
                    flag = False
                    break
            if flag:
                print(num,end=" ")
                count +=1
            num +=1
        print()
number = int(input("Enter number"))
prime_leftPyramid(number)