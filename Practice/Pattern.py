# n = ["a","b","c","d","e","f"]
# for i in range(n):
#     print("1"*(n-i) + "*" * (i+1))


for i in range(6,0,-1):
    accending=""
    # print(" " * (6 +i), end="")
    for j in range(i):
        accending += chr(65 + j)

    # print(" " * (6 +i), end="")
    descending = accending[-2::-1]
    # print(" " * (6 +i), end="")

    print(accending+(" " * (6 +i), end="")+descending)

