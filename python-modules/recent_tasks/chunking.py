def chunk(items,bags):
    result = [0 for i in range(bags)]
    if items <= bags:
        result = [1 for i in range(items)]
        print(result)
        return
    e = int(items/bags)
    r = items%bags
    # for i in range(bags):
    #     result.append(e)
    result = [e for i in range(bags)]
    for i in range(r):
        result[i] += 1
    print(result)
    return

if __name__ == "__main__":
    items = int(input("Enter no of items : "))
    bags = int(input("Enter no of bags : "))
    chunk(items,bags)