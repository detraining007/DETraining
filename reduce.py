li= [1,2,3,4,5,6,54,49,3197,499,277,699,34
,678]
new_list = [i for i in li if i % 2 == 0]
even_list = filter(lambda x : x % 2 == 0, li)
odd_list = filter(lambda x : x % 2 != 0, li)
print(new_list)
print(list(even_list))
print(list(odd_list))