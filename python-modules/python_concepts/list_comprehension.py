# list1 = [2,45,78,4,98]
# list7  =[4,6,8,8,0]
# istead of multiple lines of code usig loops
# can be written in short / compressed manner using list compreshension

# list2 = [i for i in list1 if i%2==0]
# list3 = [i for i in list1 if i%2!=0]
# list4 = [i for i in list1]
# print(list2)
# print(list3)
# print(list4)

# list5 = [print(i,j) for i in list1 for j in list7]

# print(len(list5))

l1 = [1,2,3,4]
l2 = [1,2,3,4,57,7]

l3 = [i+j for i,j in zip(l1,l2)]
# print(l3)
