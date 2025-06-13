#Example program for list comprehension

lst=[1,2,3,4,5,6,7,8,9,10]

#To print even number list
even_list=[num for num in lst if num%2==0]
print("The list of even numbers are: ",even_list)

#To print Odd number list
odd_list=[num for num in lst if num%2==1]
print("The list of odd numbers are: ",odd_list)

#To print the list after add 10 to each element
add_ten=[num+10 for num in lst ]
print("The list after adding 10 to each element",add_ten)