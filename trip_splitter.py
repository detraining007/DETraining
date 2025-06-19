# Trip Expense Splitter - Fair Expense Sharing

# Step 1: Input expense data
expenses = [
    {"name": "maneesh", "amount": 2500},
    {"name": "hari", "amount": 1500},
    {"name": "harsha", "amount": 4000}
]

# Step 2: Calculate total amount and fair share
total_amount = sum(person["amount"] for person in expenses)
num_people = len(expenses)
fair_share = total_amount / num_people

print(f"\nTotal Expense: ₹{total_amount}")
print(f"Each person's fair share: ₹{fair_share:.2f}")

# Step 3: Calculate how much each person owes or is owed
balances = {}

for person in expenses:
    name = person["name"]
    paid = person["amount"]
    balances[name] = round(paid - fair_share, 2)

# Step 4: Create list of debtors and creditors
creditors = []
debtors = []

for name, balance in balances.items():
    if balance > 0:
        creditors.append([name, balance])  # They should receive
    elif balance < 0:
        debtors.append([name, -balance])   # They should pay

# Step 5: Settle balances
print("\n--- Settlement Details ---")
i, j = 0, 0

while i < len(debtors) and j < len(creditors):
    debtor_name, debtor_amt = debtors[i]
    creditor_name, creditor_amt = creditors[j]
    
    settled_amt = min(debtor_amt, creditor_amt)
    
    print(f"{debtor_name} pays ₹{settled_amt:.2f} to {creditor_name}")
    
    debtors[i][1] -= settled_amt
    creditors[j][1] -= settled_amt
    
    if debtors[i][1] == 0:
        i += 1
    if creditors[j][1] == 0:
        j += 1
