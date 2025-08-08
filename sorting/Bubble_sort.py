def bubble_sort(arr2):
    temp = 0
    array_length = len(arr2)
    for iterable in range(array_length-1):
        swap = False
        for value in range(array_length-1):
          if arr2[value] > arr2[value+1]:
              temp = arr2[value]
              arr2[value] = arr2[value+1]
              arr2[value+1] = temp
              swap = True
        if swap== False:
              break
    return arr2









if __name__ == "__main__":
    arr1 = list(map(int,input("Enter the values in array with space: ").split()))
    print(f'Array before swapping is {arr1}')
    print("Array after swapping:")
    print(bubble_sort(arr1))