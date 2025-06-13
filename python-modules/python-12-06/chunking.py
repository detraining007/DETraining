def chunk(items,bags):
    result = list
    if items <= bags:
        result = [1 for i in range(items)]
        print(result)
        return
    e = int(items/bags)
    r = items%bags
    # for i in range(bags):
    #     result.append(e)
    result = [int(items/bags) for i in range(bags)]
    for i in range(r):
        result[i] += 1
    print(result)
    return

chunk(34,5)