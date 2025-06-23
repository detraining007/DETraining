def prime_numbers(number):
    lst =[]
    for num in range(2,number):
        count =1
        for n in range(2,number):
            if num%n ==0:
                count +=1
        if count==2:
            lst.append(num)
    print(lst)
number = int(input("Enter number"))
prime_numbers(number)
# for i in result:
#      print(i)