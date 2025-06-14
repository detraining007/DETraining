import random
lis=['','ROCK','PAPER','SCISSOR']
computer=random.choice(lis)
c_w=0
u_w=0
while True:
    inp=int(input("Enter an input '1:Rock' '2:Paper' '3:Scissor':"))
    inp=lis[inp]
    a=inp.upper()
    if a == computer :
        print(F'Draw,{a}{computer}')
        if a:=input('Do you want to continue Y or N:') == 'Y':
            pass
        else :
            break
          
    elif (a == 'ROCK') and (computer == 'PAPER') :
        print(f'Computer Wins,{a}{computer}')
        c_w+=1
        if a:=input('Do you want to continue Y or N:') == 'Y':
            pass
        else :
            break
    elif (a=='PAPER') and (computer == 'SCISSOR') :
        print(f'Computer Wins,{a}{computer}')
        c_w+=1
        if a:=input('Do you want to continue Y or N:') == 'Y':
            pass
        else :
            break
    else:
        print(f'User Wins,{inp}{computer}')
        u_w+=1
        if a:=input('Do you want to continue Y or N:') == 'Y':
            pass
        else :
            break
print(F'computer wins {c_w} User wins{u_w}')
print()
        

 
    
