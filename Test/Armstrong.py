def Arm(num):
    temp=[]
    oig = num
    while(num>0):
     og = num
     num = num//10
     rem = og%10
     temp.append(rem)
    
    temp_len = len(temp)
    for val in range(temp_len):
       temp[val] = temp[val]**temp_len
    
    sum =0
    for  val in range(len(temp)):
       sum += temp[val]
    print(sum)

    if(sum==oig):
       print(f'{oig} is an armstrong number')
    else:
       print(f'{oig} is not an armstrong number')












if __name__ == "__main__":
    num = int(input('Enter the number'))
    print(Arm(num))
