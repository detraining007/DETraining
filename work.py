
friends = ["chandu", "krishna", "vardhan", "kumar","sai"]

expenses = [
    ("kumar", 120, "Hotel"),
    ("krishna", 60, "Dinner"),
    ("Chandu", 40, "Taxi"),
    ("vardhan", 80, "Activity"),
    ("sai", 20, "Snacks"),
]
paid = {friend: 0 for friend in friends}
for payer, amount, desc in expenses:
    paid[payer] += amount

