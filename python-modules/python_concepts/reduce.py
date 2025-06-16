from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)  # 10

max_val = reduce(lambda a, b: a if a > b else b, nums)  # 4

# with initializer
reduce(lambda x, y: x + y, nums, 100)  # 110

'''

reduce() is used to reduce an iterable to a single value by applying a binary function cumulatively to the elements from left to right.
It's part of functools module in Python 3+.

Syntax:
reduce(function, iterable[, initializer])
function: A function that takes two arguments.
iterable: List, tuple, etc.
initializer (optional): Starting value (used as the first argument).

Return Type:
Returns a single value (not an iterator).

How it works:
If iterable = [a, b, c, d], 
then:
reduce(func, iterable) → func(func(func(a, b), c), d)

Common Use Cases:
Sum / Product / GCD / LCM
Factorial calculation
String concatenation
Custom accumulations (max, min, flatten list)

Performance:
Fast and memory-efficient for cumulative operations.
Comparable to for loops in speed but often less readable.
Slightly faster than for loops for large sequences when using built-ins or compiled lambda logic.

Best Practices:
Use reduce() when:
You need a single output value from a sequence.
The operation is naturally cumulative (e.g., sum, product).
Avoid for complex operations → use for loops or comprehensions for clarity.
Always import from functools in Python 3+.

When to Use:
Perfect for:
Chaining values (sum/product)
Accumulating from left to right
Functional programming style

Avoid if:
Logic involves conditions, state changes, or nested structures
Readability matters more than compactness
'''