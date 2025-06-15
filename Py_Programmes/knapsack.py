def knapsack():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)

    table = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weights[i-1] <= w:
                include = values[i-1] + table[i-1][w - weights[i-1]]
                exclude = table[i-1][w]
                table[i][w] = max(include, exclude)
            else:
                table[i][w] = table[i-1][w]

    print("Maximum value you can carry in the bag:", table[n][capacity])
knapsack()
