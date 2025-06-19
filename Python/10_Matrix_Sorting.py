from Bubble_Sort import B_Sort

n = 3
m1 = [[10,1,5],[4,8,9],[2,3,7]]
m2 = [[0,0,0] for _ in range(n)]
print(m2)

flat = []
for i in range(n):
    for j in range(n):
        flat.append(m1[i][j])
flat = B_Sort(flat)
print(flat)


k = 0
for i in range(n):
    for j in range(n):
        m2[i][j] = flat[k]
        k+=1
print("After sorting:")
print(m2)        
