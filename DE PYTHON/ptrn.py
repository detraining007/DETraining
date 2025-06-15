str = "ABCDEF"
print(str + str[4::-1])
for i in range(1, len(str)):
    left = str[:len(str) - i]
    right = left[::-1]
    spaces = " " * (2 * i - 1)  
    print(left + spaces + right)



   
        