list1 = [1,6,3,2,7,9,8,0,4]

even = lambda x : x % 2 == 0
list2 = list(filter(even,list1))
print(list2)
list3 = list(filter(lambda x : x % 2 != 0, list1))
print(list3)