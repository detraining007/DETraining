
# Keep even numbers
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# Remove empty strings
words = ["a", "", "b", "", "c"]
cleaned = list(filter(None, words))  # ['a', 'b', 'c']



'''

filter() is a built-in function used to extract elements from an iterable that satisfy 
a condition (return True) defined by a function.

Syntax:
filter(function, iterable)

function: Returns True/False for each element.
iterable: List, tuple, string, etc.
Returns a filter object (lazy iterator).

Return Type:
Returns a lazy filter object (like a generator).
Convert using list(), tuple(), or iterate with for.

Behavior:
Applies the function to each item in the iterable.
If the function returns True, the item is kept.
If function is None, it removes all falsy values (0, False, None, '').

Use Cases:
Data cleaning (remove nulls, zeros, etc.)
Functional programming (with lambda)
Filtering from logs, datasets, or input streams

Performance:
filter() is more efficient than for loops when paired with lambda, especially on large iterables.
Uses lazy evaluation, so it avoids processing the whole iterable at once (good for memory).

Best Practices:
Use when filtering logic is short (use with lambda or simple named functions).
Use with None to clean out falsy values.
For readability, prefer list comprehensions if logic is simple

Comparison: filter() vs List Comprehension
Feature	                  filter()	                                List Comprehension
Readability	              Moderate (especially with lambda)	        High
Flexibility	              Limited (1 condition only)	            Very flexible
Lazy Evaluation	          Yes	                                    No (creates full list immediately)
Performance	              Slightly better on huge data	            Better readability for small tasks

'''