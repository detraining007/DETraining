
list1 = [1,6,3,2,7,9,8,0,4]

even = lambda x : x % 2 == 0
list2 = list(filter(even,list1))
print(list2)
list3 = list(filter(lambda x : x % 2 != 0, list1))
print(list3)



'''

lambda arguments: expression

lambda is the keyword.
arguments are like parameters to a normal function.
expression is a single expression (no statements) that gets returned.

Use Cases:
Passed as a function to:
map(), filter(), sorted(), reduce()
Inside list comprehensions or UI callbacks
Data processing pipelines

Returns:
Always returns a function object that can be called.

Performance:
*Faster than def functions in terms of lookup time for small one-liners.
*But no major speed-up in practical scenarios on large datasets — the real bottleneck is usually in logic, not function call.
*Lambda + built-in functions (like map/filter) can be slightly faster than for-loops or named function combos, especially in 
 functional-style pipelines.

Limitations:
Only one expression, no multiple statements.
Cannot contain return, print, assignments.
Not reusable or debuggable like def.

Best Practices:
Use for short, one-time operations.

Avoid if:
Logic is complex
You need debugging or reuse
You need readability (especially in large codebases)

Feature	                lambda	                       def
Name	              Anonymous	                      Named
Lines	              One expression only	          Multiple statements
Readability           Less readable	                  More readable
Reusability	          No	                          Yes
Use case	          Short, inline functions	      Full-featured functions
'''