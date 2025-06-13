def generate_items(n):
    for i in range(n):
        yield(i)

for i in generate_items(10):
    print(i)