names = ['Alice', 'Bob']
scores = [85, 90]
print(list(zip(names, scores)))  # [('Alice', 85), ('Bob', 90)]

dict(zip(names, scores))  # {'Alice': 85, 'Bob': 90}

matrix = [[1, 2], [3, 4], [5, 6]]
transposed = list(zip(*matrix))  # [(1, 3, 5), (2, 4, 6)]

'''
zip() is a built-in function that combines multiple iterables element-wise into tuples — like zipping the teeth of a zipper.

Syntax:
zip(iterable1, iterable2, ...)

Takes two or more iterables.
Returns an iterator of tuples, where each tuple contains the i-th element from each iterable.

Return Type:
Returns a zip object (lazy iterator).
Use list(), tuple(), or loop to access contents.

Length Behavior:
Stops at the shortest iterable.

a = [1, 2, 3]
b = ['x', 'y']
print(list(zip(a, b)))  # [(1, 'x'), (2, 'y')]

Unzipping (Reverse Zip):
Use unpacking with zip(*):

pairs = [(1, 'a'), (2, 'b')]
a, b = zip(*pairs)
print(a)  # (1, 2)
print(b)  # ('a', 'b')

Use Cases:
Parallel iteration over multiple sequences.
Combining keys and values.
Creating tuples of paired data.
Transposing matrices.
Unpacking grouped data.

Best Practices:
Always convert the result if you need to view or reuse it (e.g., list(zip(...))).
Use in for loops for clean parallel iteration:
for name, score in zip(names, scores):
    print(name, score)

Comparison: zip() vs Manual Indexing
# Using zip (recommended)
for a, b in zip(list1, list2): ...

# Manual indexing (longer, error-prone)
for i in range(len(list1)): ...

zip() is cleaner, safer, and more readable.

'''