class TripExpenseManager:
    def __init__(self):
        self.expenses = {}

    def input_expenses(self):
        n = int(input("Enter number of students on the trip: "))
        for _ in range(n):
            name = input("Enter student name: ")
            amount = float(input(f"Enter amount paid by {name}: "))
            self.expenses[name] = amount

    def calculate_balances(self):
        n = len(self.expenses)
        total = sum(self.expenses.values())
        fair_share = total / n
        self.balances = {}

        for name, paid in self.expenses.items():
            self.balances[name] = round(fair_share - paid, 2)

        print(f"\n📊 Total Trip Expense: ₹{total:.2f}")
        print(f"💰 Each student's share: ₹{fair_share:.2f}\n")
        return self.balances

    def settle_balances(self):
        debtors = {}
        creditors = {}

        for name, balance in self.balances.items():
            if balance > 0:
                debtors[name] = balance
            elif balance < 0:
                creditors[name] = -balance  # convert to positive for processing

        print("🔄 Settlement Instructions:\n")
        debtor_names = list(debtors.keys())
        creditor_names = list(creditors.keys())

        i, j = 0, 0
        while i < len(debtor_names) and j < len(creditor_names):
            d_name = debtor_names[i]
            c_name = creditor_names[j]
            d_amt = debtors[d_name]
            c_amt = creditors[c_name]

            settled_amt = min(d_amt, c_amt)
            print(f"➡️ {d_name} pays ₹{settled_amt:.2f} to {c_name}")

            debtors[d_name] -= settled_amt
            creditors[c_name] -= settled_amt

            if debtors[d_name] == 0:
                i += 1
            if creditors[c_name] == 0:
                j += 1

# ===============================
# 🎒 Class Trip Manager Execution
# ===============================

trip = TripExpenseManager()
trip.input_expenses()
trip.calculate_balances()
trip.settle_balances()
