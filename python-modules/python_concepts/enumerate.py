
my_list = ["apple", "orange", "banana"]
for i, value in enumerate(my_list):
    print(i,value)

#With Custom Start Index:
for i, item in enumerate(['a', 'b'], start=1):
    print(i, item)
# 1 a
# 2 b

'''

enumerate() adds a counter/index to an iterable, returning pairs of (index, item) — often used in loops where you need both index and value.

Syntax:
enumerate(iterable, start=0)

iterable: List, tuple, string, etc.
start: Optional, default is 0.

Return Type:
Returns an enumerate object (lazy iterator).
Use list() to view:
a = ['x', 'y']
print(list(enumerate(a)))  # [(0, 'x'), (1, 'y')]

Use Cases:
When looping and needing the index along with the value
Labeling outputs (e.g., numbering questions, rows)
Replacing manual indexing (range(len(...)))

Performance:
Highly efficient and memory-safe (lazy evaluation).
Much faster and cleaner than manual indexing.

Best Practices:
Prefer enumerate() over range(len(...)) for better readability and Pythonic code.
Use start=1 when human-readable counting is needed.

Comparison: enumerate() vs range(len(...))
Feature	          enumerate()	                   range(len(...))
Readability	      High (clean + explicit)	      Less readable
Error-prone	      Less (no indexing mistakes)	  More (index mismatch risk)
Performance	      Faster (internally optimized    Slightly slower


'''