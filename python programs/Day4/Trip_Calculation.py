trip_members = ["Ramu","Harish","Ashok","Mahesh"]
amount_collected = {"Ramu":2000,"Harish":3000,"Ashok":2500,"Mahesh":1500}
estimation = 8000
total_amount = sum(amount_collected.values())
print(f"Total amount collected {total_amount}")

# Amount used
money_spent ={"travel":3500,"food":1500,"rent":1000,"others":2450}
total_spent = sum(money_spent.values())
print(f"Total money spent {total_spent}")

# Calculations
if estimation < total_spent:
    print("Bad estimation for trip")
else:
    print("Good estimation")

equal_share = float(total_spent/len(trip_members))
difference = total_amount - total_spent

print(f"Equal share for each person is {equal_share}")

#Amount Summary

for name in trip_members:
    paid = amount_collected[name]
    balance = paid - equal_share
    status = "Get back" if balance > 0 else "needs to add"
    print(f"{name}: Paid {paid} so {status} to be {abs(balance)}")

