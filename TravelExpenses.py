# Step 1: Input names
friends = input("Enter the names of all friends, separated by commas: ").strip().split(",")
friends = [f.strip() for f in friends if f.strip()]
n = len(friends)

# Step 2: Input expenses
expenses = {name: 0 for name in friends}
while True:
    payer = input("\nWho paid? (or type 'done' to finish): ").strip()
    if payer.lower() == "done":
        break
    if payer not in friends:
        print("Name not in friends list. Try again.")
        continue
    try:
        amount = float(input("How much did they pay? "))
    except ValueError:
        print("Invalid amount. Try again.")
        continue
    expenses[payer] += amount

# Step 3: Calculate total and fair share
total = sum(expenses.values())
share = total / n

print("\nTotal expenses: ₹{:.2f}".format(total))
print("Each person's share: ₹{:.2f}".format(share))

# Step 4: Show who owes or is owed
balances = {name: expenses[name] - share for name in friends}
for name, bal in balances.items():
    if bal > 0:
        print(f"{name} is owed ₹{bal:.2f}")
    elif bal < 0:
        print(f"{name} owes ₹{abs(bal):.2f}")
    else:
        print(f"{name} is settled up.")

# Step 5: (Optional) Simple settlement suggestion
print("\n--- Suggested Settlements ---")
debtors = [(name, -bal) for name, bal in balances.items() if bal < 0]
creditors = [(name, bal) for name, bal in balances.items() if bal > 0]
i, j = 0, 0
while i < len(debtors) and j < len(creditors):
    debtor, debt = debtors[i]
    creditor, credit = creditors[j]
    pay = min(debt, credit)
    print(f"{debtor} pays {creditor}: ₹{pay:.2f}")
    debtors[i] = (debtor, debt - pay)
    creditors[j] = (creditor, credit - pay)
    if debtors[i][1] < 0.01:
        i += 1
    if creditors[j][1] < 0.01:
        j += 1
