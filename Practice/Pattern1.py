# print(chr(65))

num = 6
for i in range(num,0,-1):
    asce = ""
    for j in range(i):
        asce=asce+chr (65 + j)
        desc = asce[-2::-1]
    print(j)
    print(asce+" "+desc)
    # print("")
    # print(desc)

