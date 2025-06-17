n=int(input("enter the number of members went for trip"))
d=["Travelling","Journey","Food","Accomodation","Activities"]
amount_list=[0 for i in range(0,n)]
for i in range(1,n+1):
      print(i)
total_amount=0
for _ in d:
    c=input("enter the expense name: ")
    if  c in d:
            amount = int(input(f"Enter the amount spent on {c}:"))
            person=int(input("enter the name of person as 0,1,2....:"))
            amount_list[person]+=amount
            total_amount+=amount
share=total_amount//n
print(f"the total amount is: {total_amount}")
print(f"the share for each person is:{share}")
m=n-1
for i in range(0,n):
      x=amount_list[i]-share
      if x<0:
            x=-1*(x)
            print(f"number {i} person should give {x//m} to each one")
      elif(x==0):
            print(f"The person{i}don't need to contribute anymore money ")

      else:
            print(f"{m}people owes to  number {i} person a amount of {x//m} each")