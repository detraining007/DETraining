bags = int(input("Enter the no of bags: "))
balls = int(input("Enter the no of balls: "))

x = balls // bags # equal parts
y = balls % bags  # remainder

seq = [] #empty list to iterate

for i in range(1, bags + 1):
    if i <= y:
        seq.append(x + 1) #appends  equal parts and remainder
    else:
        seq.append(x) #appends  equal parts only

for i in range(bags):
    if seq[i] != 0: # check condition if bags are not empty
        print(f"Bag {i+1} has {seq[i]} balls")

