def knapsack(chunks,items):
    if chunks > items:
        chunks = min(chunks,items)
        #print(f"{chunks} are greater than {items},chunks must be less than items!")
    values = items//chunks
    remaining_values = items%chunks
    target = []
    start = 0
    #now we will add remaining items to chunks
    for rem in range(chunks):
        target.append(values)
    while(remaining_values>0):
         target[start] += 1
         start += 1
         remaining_values -= 1
    print(target)




if __name__ == "__main__":
    chunks = int(input("Enter the no of chunks: "))
    items = int(input("Enter the no of items u want to insert in bags: "))
    print("in this way items can be loaded into chunks: ")
    print(knapsack(chunks,items))