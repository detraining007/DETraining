n=4
people=['A','B','C','D']
expences=['food','accomodation','travel','activities']
food=int(input("enter food cost:"))
accomodation=int(input("enter acc cost:"))
travel=int(input("enter travel cost:"))
activities=int(input("enter others cost:"))
total=food+accomodation+travel+activities
share=total//n
if total%n!=0:
    r=(total%n)//n
    print("shared amount:",r)
else:
    print("shared amount per person=",share)
    balance={'A':food-share, 
            'B':accomodation-share, 
            'C':travel-share, 
            'D':activities-share}
    print("Balance for each: ",balance)