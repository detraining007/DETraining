friends=int(input("Enter Number of peoples"))
expense=[]
while True:
    pay=input("You want to Pay something (yes or No):")
    if pay=="Yes":
        name=input("Enter Name:")
        cost=int(input("Enter Money:"))
        item=input("Enter item:")
        expense.append((name,cost,item))
    else:
        print("It's ok no problem")
        break
    
    for name, cost, item in expense:
        print(f"{name} paid ${cost:.2f} for {item}")
        
    print(expense)
def dist():
    print("Here, Each persons Share of total amount")
    total_Money=0
    paid_people={}
    for name,cost,item in expense:
        total_Money+=cost
        paid_people[name]=cost
        share=total_Money//friends

    print(f"Total Money spent:,{total_Money}") 
    print(f"Each person share:{share}")

    for name in paid_people:
        pay=paid_people[name]
        balance=pay-share
        if balance>0:
            print(f"{name} will recive {balance}")
        elif balance<0:
            print(f"{name} will pay {-balance}")
        else:
            print(f"{name} is settled")

dist()

