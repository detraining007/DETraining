from functools import reduce

list_num =[1,2,3,4,5,6,7,8,9]
odd_num = list(filter(lambda x: x%2!=0 , list_num))
print(odd_num)

odd_nums = reduce(lambda x,y: x+y, list_num)
print(odd_nums)

sqrt_list = list(map(lambda x : x*x, list_num))
print(sqrt_list)