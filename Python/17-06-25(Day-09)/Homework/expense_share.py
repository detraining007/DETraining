#To find a fair and efficient way to share expenses among group of friends

# dict={}

# Step 1: Input the expenses
n = int(input("Enter number of friends: "))
expenses = {}

for i in range(n):
    name = input("Enter name: ")
    amount = float(input(f"Amount paid by {name}: "))
    expenses[name] = amount

# Step 2: Calculate total and fair share
total = sum(expenses.values())
share = total / n

print(f"\nTotal: ₹{total:.2f}")
print(f"Each should pay: ₹{share:.2f}\n")

# Step 3: Show who owes or gets back money
for name, paid in expenses.items():
    balance = round(share - paid, 2)
    if balance > 0:
        print(f"{name} owes ₹{balance:.2f}")
    elif balance < 0:
        print(f"{name} gets back ₹{-balance:.2f}")
    else:
        print(f"{name} is settled up.")
