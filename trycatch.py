try:
    n=[1,2,3,4,5]
    print(n[7])
except IndexError:
    print("index out of bound")
finally:
    print("end")
