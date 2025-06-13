def segregate(lst2):
    even = []
    odd = []

    is_even = lambda value: value%2==0
    is_odd = lambda value: value%2!=0
    for value in lst2:
        if is_even(value):
           even.append(value)
        else:
           odd.append(value)
    print(f'The even numbers in list are {even}')
    print(f'The odd numbers in list are {odd}')
    





if __name__ == "__main__":
    print("Enter a list of values")
    lst = [3,7,10,12,18,45]
    print(segregate(lst))

