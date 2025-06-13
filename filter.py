#using list comprehension with the filter method

lst=[1,2,3,4,5,6,7,8,9,10]

#To print even number list with list comprehension using lambda and filter functions
even_lst=list(filter(lambda x: x%2==0, lst))
print("List of even numbers: ",even_lst)

#to print odd number list with list comprehension using lambda and filter function
odd_lst=list(filter(lambda x: x%2!=0,lst))
print("List of odd numbers: ",odd_lst)