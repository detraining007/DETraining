def balanced_chunking(items, buckets):
    base = items // buckets
    extra = items % buckets

    result = []

    for i in range(buckets):
        if i < extra:
            result.append(base + 1)
        else:
            result.append(base)

    return result

# Example usage
items = int(input("Enter number of items: "))
buckets = int(input("Enter number of buckets: "))
print("Distribution:", balanced_chunking(items, buckets))
