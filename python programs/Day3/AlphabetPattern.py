number = int(input("enter number"))
num = number
list = []

size = (number*2)-1
if(0<number > 26):
    raise ValueError("Number cant be greater than 26")
else:
    for i in range(size):
      if number >0:
       list.append(chr(65+i))
      else:
          list.append(chr(65+(size-(i+1))))
      number -= 1
for row in range(num,0,-1):
    for column in range(row):
        print(list[column],end=" ")
    spaces = (num-row)*4
    print( " "* spaces,end="")
    for column in range(row):
        print(list[(column+num)-1],end=" ")
    print()




