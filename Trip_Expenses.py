def trip_expenses(Trip,People):
    Total = int(input("Enter the total expenses happened for the trip:"))
    original_total = Total
    Budget = {}
    settlements = {}
    debit = []
    credit = []
    for share in range(len(People)):
        while(Total !=0 and share<len(People)):
            amount = int(input(f"Please enter the amount less than {Total} for {People[share]} spent on {Trip[share]}: "))
            if(amount<=Total):
             Budget[People[share]] =  amount
             Total -= amount
             share += 1
            else:
               print(f'Amount:{amount} should be less than Total:{Total}')
    for key,item in Budget.items():
        print(f"{key}:{item}")
    average = original_total//len(People)
    print(f'Average amount is {average}')
    for key,items in Budget.items():
       if(Budget[key]<=average):
          debit.append(key)
       elif(Budget[key]>average):
          credit.append(key)
    for val in People:
       balance =  Budget[val] - average
       if(balance<0):
          settlements[val] = balance
       elif(balance>=0):
          settlements[val] = balance
    for key,item in settlements.items():
        print(f'{key}:{item} ')
    for person,debt in settlements.items():
       if(debt<0):
          print(f'{person} owes debt of Rupees {abs(debt)} to')
          for val in credit:
             print(val)
          
          
    





if __name__ == "__main__":
    Trip = list(map(str,input("Please enter the sections of the trip: ").split()))
    People = list(map(str,input("Please enter the name of people who were in the trip: ").split()))
    print(trip_expenses(Trip,People))