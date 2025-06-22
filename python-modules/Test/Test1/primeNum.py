
def prime(s,e):
    res = []
    for num in range(s,e+1):
        cnt = 0
        for i in range(2,int(num/2 + 1)):
            if num % i == 0:
                cnt += 1
        if cnt < 1:
            res.append(num)
    return res

print(prime(4,10))