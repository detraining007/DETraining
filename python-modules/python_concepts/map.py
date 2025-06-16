
nums = [1, 2, 3]
squares = map(lambda x: x**2, nums)
print(list(squares))  # [1, 4, 9]

# With Multiple Iterables:
a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))  # [5, 7, 9]

#You can chain map() and filter() for functional-style data processing:
nums = [1, 2, 3, 4, 5]
squares_of_even = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))  # [4, 16]

'''
map() is a built-in function that applies a function to each item of an iterable (or multiple iterables), 
and returns a new iterator with the results.

Syntax:
map(function, iterable)

function: A function that transforms each item.
iterable: One or more sequences (e.g., list, tuple).
Returns a map object (iterator).

Return Type:
Returns a lazy map object.
Convert using list(), tuple(), or loop.


Use Cases:
Apply transformations: squaring, formatting, parsing
Clean/convert data: str(), int(), float(), round()
Combine multiple iterables (with lambda)

Performance:
Faster than loops for large data sets due to internal optimization.
More memory efficient than list comprehensions (lazy evaluation).
Especially fast with built-in functions like str, int, round.

Best Practices:
Use map() for simple one-to-one transformations.
Combine with lambda for quick anonymous logic.
Avoid complex logic inside lambda; use named functions instead.
Convert result (map object) only when needed (defer computation).

Comparison: map() vs List Comprehension
Feature	                              map()	                            List Comprehension
Readability	                          Good with simple functions	    Better for most use cases
Supports multiple iterables	          Yes	                            Not directly
Lazy Evaluation	                      Yes (iterator)	                No (eager list)
Performance	                          Slightly better with built-ins	More readable for complex logic

'''