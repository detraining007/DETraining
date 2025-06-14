from random import *
n=int(input("enter a number:"))
shuffle_lst=[i for i in range(1,(n*n)+1)]
sort_lst=shuffle_lst.copy()#sorted list in l1
shuffle(shuffle_lst)#shuffling
x=sample(shuffle_lst,1)#taking random no
for i in x:
    x1=i

sort_lst=["_" if i==x1 else i for i in sort_lst] #sorted list lo -1 at pos of random number

for i in range(0,n*n):#replacing random no with -1
    if shuffle_lst[i]==x1:
        shuffle_lst[i]="_"

shuffle_2d=[shuffle_lst[i:i+n] for i in range(0,n*n,n)]
sort_lst_2d=[sort_lst[i:i+n] for i in range(0,n*n,n)]

print("***THE ORIGINAL 2D LIST IS:***")
for i in range(0,n):#shuffle list printing and taking index of -1
    for j in range(0,n):
        print(sort_lst_2d[i][j],end=" ")
        if sort_lst_2d[i][j]=="_":
            r,c=i,j
    print("\n")


print("***THE SHUFFLED 2D LIST IS:***")
for i in range(0,n):#shuffle list printing and taking index of -1
    for j in range(0,n):
        print(shuffle_2d[i][j],end=" ")
        if shuffle_2d[i][j]=="_":
            r,c=i,j
    print("\n")

print(f"initial space value is at: {r},{c}")#row and column value of -1


def up(r,c,shuffle_2d):
    shuffle_2d[r][c],shuffle_2d[r-1][c]=shuffle_2d[r-1][c],shuffle_2d[r][c]
    return r-1
def down(r,c,shuffle_2d):
    shuffle_2d[r][c],shuffle_2d[r+1][c]=shuffle_2d[r+1][c],shuffle_2d[r][c]
    return r+1
def left(r,c,shuffle_2d):
    shuffle_2d[r][c],shuffle_2d[r][c-1]=shuffle_2d[r][c-1],shuffle_2d[r][c]
    return c-1
def right(r,c,shuffle_2d):
    shuffle_2d[r][c],shuffle_2d[r][c+1]=shuffle_2d[r][c+1],shuffle_2d[r][c]
    return c+1
con=1
while(con):
    u=0#up
    d=0#down
    ri=0#right
    le=0#left
    for i in range(0,n):
        for j in range(0,n):
            if shuffle_2d[i][j]=="_":
                if  i-1 >= 0:
                    u=1 
                if i+1 < n:
                    d=1
                if j+1 < n:
                    ri=1
                if j-1 >= 0:
                    le=1
    print(f"operations that can be done {u},{d},{ri},{le}")
    if u == 0 and d == 1 and ri == 1 and le == 0:
        choice=input("You can go down or right ? Enter your choice:")
        if choice=="down":
            r=down(r,c,shuffle_2d)
        elif choice=="right":
            c=right(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 0 and d == 1 and ri == 0 and le == 1:
        choice=input("You can go down or left ? Enter your choice:")
        if choice=="down":
            r=down(r,c,shuffle_2d)
        elif choice=="left":
            c=left(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 1 and d == 0 and ri == 1 and le == 0:
        choice=input("You can go up or right ? Enter your choice:")
        if choice=="up":
           
            r=up(r,c,shuffle_2d)
        elif choice=="right":
            c=right(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 1 and d == 0 and ri == 0 and le == 1:
        choice=input("You can go up or left ? Enter your choice:")
        if choice=="up":
            r=up(r,c,shuffle_2d)
        elif choice=="left":
            c=left(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 1 and d == 1 and ri == 1 and le == 1:
        choice=input("You can go up or  down or right or left  ? Enter your choice:")
        if choice=="up":
            r=up(r,c,shuffle_2d)
        elif choice=="right":
            c=right(r,c,shuffle_2d)
        elif choice=="down":
            r=down(r,c,shuffle_2d)
        elif choice=="left":
            c=left(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 1 and d == 0 and ri == 1 and le == 1:
        choice=input("You can go up or right or left  ? Enter your choice:")
        if choice=="up":
            r=up(r,c,shuffle_2d)
        elif choice=="right":
            c=right(r,c,shuffle_2d)
        elif choice=="left":
            c=left(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 1 and d == 1 and ri == 1 and le == 0:
        choice=input("You can go up or down or right ? Enter your choice:")
        if choice=="up":
            r=up(r,c,shuffle_2d)
        elif choice=="right":
            c=right(r,c,shuffle_2d)
        elif choice=="down":
            r=down(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 1 and d == 1 and ri == 0 and le == 1:
        choice=input("You can go up or down or left  ? Enter your choice:")
        if choice=="up":
            r=up(r,c,shuffle_2d)
        elif choice=="down":
            r=down(r,c,shuffle_2d)
        elif choice=="left":
            c=left(r,c,shuffle_2d)
        else:
            print("invalid choice")
    if u == 0 and d == 1 and ri == 1 and le == 1:
        choice=input("You can go  down or right or left  ? Enter your choice:")
        if choice=="right":
            c=right(r,c,shuffle_2d)
        elif choice=="down":
            r=down(r,c,shuffle_2d)
        elif choice=="left":
            c=left(r,c,shuffle_2d)
        else:
            print("invalid choice")
    print("*** SHUFFLE LIST AFTER A OPERATION:***")
    for i in range(0,n):#shuffle list after operation
        for j in range(0,n):
            print(shuffle_2d[i][j],end=" ")
        print("\n")
    check=0
    for i in range(0,n):#check shuffle and original are same
        for j in range(0,n):
            if shuffle_2d[i][j]!=sort_lst_2d[i][j]:
                check=1
    if check==0:
        print("CONGRATS YOU WON")
        con=0
print("***THE PROGRAM ENDED***")                  