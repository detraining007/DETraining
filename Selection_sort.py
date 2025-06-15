def selection_sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[j]<list[i]:
                list[j],list[i]=list[i],list[j]
    return list

list=[8,10,9,7,21,1,19]
print(selection_sort(list))