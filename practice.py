#lis_1=[11,55,22,33,44]
#new_list=[i for i in lis_1 if (i%2 == 0)]
#print(new_list)*/

#l=[22,11,44,23]
#new_l=[i+10 for i in l]
#print(new_l)

#rows=4

n=[1,2,3,4,5,6,7,8]
even_numbers=list(filter(lambda i : i % 2 ==0 ,n))
print(even_numbers)

for i in even_numbers:
    print(i)


from functools import reduce
q=[1,2,3,4,6,7]
plus=reduce(lambda i,j : i+j,q)
print(plus)



def gen(k):
    yield k
    


z=[1,2,3,4,5]
sqrt=map(lambda item : item * item ,z)
print(gen(sqrt))

                                                                                                           
