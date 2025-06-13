x = [1,2,3,2,2,1,2,1,213,1,3,2,]
even_numbers = list(filter(lambda a: a % 2 == 0, x))
print(even_numbers)


from functools import reduce
num = [1,2,3,2,2,1]
result =  reduce(lambda x,y: x+y, num)
print(result)

sqr_lst = [1,2,3,4,5]
sqr_lst = list(map(lambda item: item*item, sqr_lst))
print(sqr_lst)

