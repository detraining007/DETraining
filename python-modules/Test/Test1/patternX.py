
def pattern(n):
    # for rows
    for row in range(2 * n - 1):
        # for spaces
        sp = row if row < n else 2 * n - row - 2
        for s in range(sp):
            print(' ',end=' ')
        # for stars
        st = n - row if row < n else row - n + 2
        for str in range(st):
            print(' * ',end=' ')
        print()
pattern(6)