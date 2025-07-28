li1 = []
li2 = []

n = int(input("Enter first number: "))
li1.append(n)
li1.append(id(n))

n = int(input("Enter second number: "))
li2.append(n)
li2.append(id(n))

globals_items = list(globals().items())

print(f"li1: {li1}")  # [value, id]
print(f"li2: {li2}")  # [value, id]
print("\nSearching for li1 value (first input):")

for name, value in globals_items:
    if id(value) == li1[1]:
        print(f"Found in globals: {name} = {value}")

print("\nSearching for li2 value (second input):")
for name, value in globals_items:
    if id(value) == li2[1]:
        print(f"Found in globals: {name} = {value}")
