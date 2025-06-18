def chunking(total_balls,total_bags):
    divided_balls=total_balls//total_bags
    remaining_balls=total_balls%total_bags
    bags=[(divided_balls+1)  if i < remaining_balls else divided_balls for i in range(total_bags)]
    print(bags)

Balls=int(input("ENter  No of balls:"))
Bags=int(input("ENter No of bags:"))
chunking(Balls,Bags)    