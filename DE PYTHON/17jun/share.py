def input_expenses():
    n = int(input("Enter total number of friends: "))
    expenses = {} 
# adding input in dict 
    for _ in range(n):
        name = input("Enter friend's name: ")
        name_trans = input("Enter friend paid for : ")
        amount = float(input(f"Enter amount paid by {name}: "))
        expenses[name] = amount

    return expenses
# calculate avg
def calculate_balances(expenses):
    n = len(expenses)
    total = sum(expenses.values())
    share = total / n
    balances = {}
    for name, paid in expenses.items():
        diff = share - paid  # if -ve then had to give else +ve gets 
        balances[name] = diff  
#print the total 
    print("After calculating : ")
    print(f"Total Expense: ₹{total:.2f}")
    print(f"Each person should pay: ₹{share:.2f}")
    return balances

def settle_balances(balances):
    debtors = {}
    creditors = {}

    for name, balance in balances.items():
        if balance < 0:
            debtors[name] = -balance
        elif balance > 0:
            creditors[name] = balance  

    print("Settlement Transactions:")

    debtor_names = list(debtors.keys()) # names of debtors
    creditor_names = list(creditors.keys()) # names of creditors

    i, j = 0, 0 # i,j iterate till all debitors ,creditors complete
    while i < len(debtor_names) and j < len(creditor_names):
        d_name = debtor_names[i] #names of debtors
        c_name = creditor_names[j] # names of creditors

        d_amt = debtors[d_name] # money should give
        c_amt = creditors[c_name] # money should receive

        settled_amt = min(d_amt, c_amt)
        print(f"{d_name} pays {c_name} ₹{settled_amt:.2f}")

        debtors[d_name] -= settled_amt # subtract from money
        creditors[c_name] -= settled_amt # subtract from money

        if debtors[d_name] == 0:
            i += 1
        if creditors[c_name] == 0:
            j += 1

# Run the full program
expenses = input_expenses()
balances = calculate_balances(expenses)
settle_balances(balances)
