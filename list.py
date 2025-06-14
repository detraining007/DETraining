# def min_moves(list1, list2):
#     return sum(a != b for a, b in zip(list1, list2))

# List1 = [1,2,3,4,5]
# List2 = [5,1,2,3,4]
# print(min_moves(List1, List2))  

# List1 = [1,2,3,4,5]
# List2 = [1,2,3,4,5]
# print(min_moves(List1, List2))  

# List1 = [1,2,3,4,5]
# List2 = [1,4,3,5,2]
# print(min_moves(List1, List2))

def is_sub_string(sub,main):
    lis=[]
    for i in range(len(sub)):
        for j in range(len(main)):
            if sub[i] == main[j]:
                lis.append(sub[i])
                main=main.replace(main[j],'')
                print(main)
                break
    print(lis,main)
    check=''.join(lis)
    if check == sub:
        return True
    return False

sub='sandeep'
main='ssanndep'
print(is_sub_string(sub,main))
            