lst = [ 20,30,54,43,29,7,65,4]

lst2 = list(filter(lambda odd: odd % 2!=0,lst))
print(lst2)