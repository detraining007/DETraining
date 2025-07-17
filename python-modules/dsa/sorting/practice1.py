arr  = [7,6,1,8,2,0]
n = len(arr)


for i in range(n-1):
   for j in range(n-i-1):
	   if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
	
for element in arr:
	print(element,end=' ')