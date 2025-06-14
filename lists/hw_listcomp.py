print("adding elements from 2 list")
l1=[i+j for i in [2,4,6] for j in [1,3,5]]
print(l1)
print("multiplying  elements from 2 lists")
l2=[i*j for i in [5,7,4] for j in [2,5,3]]
print(l2)
'''lambda function'''
print("using lambda to add 10 to every element in list")
f=lambda x:x+10
l3=[f(i) for i in[1,2,3,4,5]]
print(l3)
