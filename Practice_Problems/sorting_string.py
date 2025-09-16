
range = int(input("Enter how many strings u want to insert in list: "))
askagain= True
while(askagain):
    values = input("Enter the strings of the list:")
    if(len(values)!=range):
        print("Enter the strings as per the range u have given: ")
    else:
        print("Matching!")
        askagain= False
        break
lists = list(map(str,values.split(",")))
print(lists)
    


