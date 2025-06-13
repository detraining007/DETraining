# for i in range(5):
#     for j in range(i):
#         print("*",end="  ")
#     print()

# print("_________________")

# for i in range(5):
#     for j in range(5-i):
#         print("*",end="  ")
#     print()

# print("_________________")
def patterns(n):
  for row in range(n):
    for space in range(n-row):
        print(end=" ")
    for col in range(row):
        print("*",end=" ")
    print()
  for row in range(n):
    for space in range(row):
        print(end=" ")
    for col in range(n-row):
        print("*",end=" ")
    print()
def traingle(n):
   for row in range(n):
      for space in range(n-row):
        print(end=" ")
      for col in range(row):
        print("*",end=" ")
      
      print()
n=int(input())
patterns(n)
traingle(n)
