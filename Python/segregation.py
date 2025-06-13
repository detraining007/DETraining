no_of_bags = int(input("Enter the no of bags: "))
no_of_balls = int(input("Enter the no of balls: "))

bags = {}


print(no_of_balls//no_of_bags) 
x = no_of_balls//no_of_bags

for i in range(1,no_of_bags+1):
    bags[f"bag_{i}"] = x


y= no_of_balls % no_of_bags
for i in range(1,y+1):
    bags[f"bag_{i}"]+=1


for i in bags:
    print(i,bags[i])



















# for i in range(1,no_of_bags+1):
#     bags[f"bag_{i}"] += x