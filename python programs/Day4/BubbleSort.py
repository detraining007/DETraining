def bubble_Sort(arr):
     size = len(arr)
     for i in range(size-1,0,-1):
         flag = False
         for j in range(i):
             if arr[j] > arr[j+1]:
              arr[j],arr[j+1] = arr[j+1],arr[j]

              flag = True
         if not flag:
            break

arr = [20,6,99,23,5]
bubble_Sort(arr)
print(arr)

