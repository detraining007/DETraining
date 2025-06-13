#Using map method with list comprehension using map function
#To print squares of each element in the list

lst=[1,2,3,4,5]
sqt_lst=list(map(lambda num: num*num,lst))
print("The list of squared elements is: ",sqt_lst)