from functools import reduce

expenses = [["person1", 1000, 0, 500, 1000],
            ["person2", 500, 1000, 1500, 0],
            ["person3", 500, 1000, 1500, 0], 
            ["person4", 1000, 0, 500, 1500]]

title = ["name", "food", "transportation", "accommodation", "activities"]
data = [dict(zip(title,row)) for row in expenses]

for row in data:
    for t in title:
        print(t,':',row[t],end=' ')
    print()

names = [row[0] for row in expenses]

person_share = []

for i in range(len(data)):
    person_share.append(data[i]["food"]+data[i]["transportation"]+data[i]["accommodation"]+data[i]["activities"])

# Share of each person
Share = dict(zip(names,person_share))
print("\nShare of each person")
print(Share)

total_expense = reduce(lambda x,y:x+y, person_share)

avg = total_expense/len(person_share)

to_pay = [avg-ps for ps in person_share]
Pay = dict(zip(names,to_pay))

# Amount each person has to pay for final settlement
print("\nAmount each person has to pay and divide for final settlement")
print(Pay)