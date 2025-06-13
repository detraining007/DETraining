def odd_number(n):
    odd_numbers = []
    count = 0
    number = 1
    while count < n:
        if number % 2 != 0:
            odd_numbers.append(number)
            count += 1
        number += 1
    return odd_numbers


alphabets = ["A","B","C","D","E","F","G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U',"V",'W','X','Y',"Z"]


n = 9
spaces_count_list = odd_number(n)

new_list = [alphabets[j] for j in range(n)]
reverse_list = [alphabets[j] for j in range(n-2,-1,-1)]
# print(reverse_list)
for i in range(n):
    
    for j in new_list:
        print(j,end=" ")
    # print(new_list,end=" ")
    if i > 0:
        count = spaces_count_list[i-1]
        for k in range(count):
            print(" ",end=" ")
    
    for j in reverse_list:
        print(j,end=" ")
    if i >0:
        reverse_list.remove(reverse_list[0])
    new_list.pop()
    print()