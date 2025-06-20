#f1, f2, f3, f4 went to a trip
#goal is to track expenses
#calculate shares
#settle balances

# food
# transportation
# accomidation
# activities

#taking input how many friends went to trip
# frnds = int(input("enter the count of friends went to trip: "))

# food=int(input("enter the total amount paid for the food: "))
# transportation = int(input("enter the total amount paid for transportation: "))
# accomidation = int(input("enter the total amount paid for accomidation: "))
# activities = int(input("enter the amount paid for activites: "))

# Step 1: Track expenses
expenses = {
    'Pawan': 12000,   
    'Murali': 8000,      
    'Akhil': 10000  
}

# Step 2: Calculate total and share
total_expense = sum(expenses.values())
num_people = len(expenses)
fair_share = total_expense / num_people

print("Total Expense:", total_expense)
print("Fair Share per Person:", fair_share)

# Step 3: Calculate balances (who owes or is owed)
balances = {}
for person, amount_paid in expenses.items():
    balances[person] = round(amount_paid - fair_share, 2)

print("\nBalances (positive means paid more, negative means owes money):")
for person, balance in balances.items():
    print(f"{person}: {balance}")

# Step 4: Display simple settlement plan
print("\nSettlement Suggestions:")
for person, balance in balances.items():
    if balance < 0:
        print(f"{person} should pay {-balance}")






