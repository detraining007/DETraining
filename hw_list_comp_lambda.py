#List comprehension using lambda function - add 10 to all the elements of the list

#example of lambda function
func=lambda x: print(x+10)
func(5)

#To print list after adding 10 to each element using lambda function
lst=[1,2,3,4,5]
add_ten=[(lambda num:num+10)(num) for num in lst]
print(add_ten)

#To print even number list using lambda function
even_lst=[(lambda num:num%2==0)(num) for num in lst]
print("Is even number check: ",even_lst)

#code to add two elements from 2 different lists and append them in new one

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
add_list=[lst1[num]+lst2[num] for num in range (len(lst1))]
print("To print updated list: ",add_list)

#To print tuples of combination of two lists
lst3=[(num1,num2) for num1 in range(len(lst1)) for num2 in range(len(lst2))]
print("The list of tuples are: ",lst3)