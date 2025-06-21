arr = [20,3,57,1,4]
arr_len = len(arr)


for i in range(arr_len-1):
    index = i
    min = arr[i]
    for j in range(i+1,arr_len):
        # print(arr[i],arr[j])
        if arr[j] < min:
            index = j
            min = arr[j]
    arr[index] = arr[i]
    arr[i] = min
    print(arr)