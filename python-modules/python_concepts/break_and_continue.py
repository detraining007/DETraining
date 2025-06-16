# Break
# Example : To print numbers from 0 to 5

cnt = 0
while(cnt < 10):
    print(cnt)
    if(cnt == 5):
        break
    cnt += 1



# Continue
# Example : To print odd numbers between 1 and 20

for i in range(20):
    if i % 2 == 0:
        continue
    print(i, end=" ")



    # n = 4
# for i in range(1,n):
#     for j in range(1,n):
#         if(i + j >= n):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for j in range(1,n):
#         if(j < i):
#             print('*',end=' ')
#     print()
# for i in range(1,n):
#     for j in range(1,n):
#         if(j > i):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     for j in range(1,n):
#         if(i + j < n - 1):
#             print('*',end=' ')
#     print()

# def printPattern4(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print(' ',end=' ')
#         c = i
#         for j in range(c,0,-1):
#             print(j,end=' ')
#         for j in range(2,i+1):
#             print(j,end=' ')
#         print()