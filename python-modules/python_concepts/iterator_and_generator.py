
#Example of an iterator:
nums = [1, 2, 3]
it = iter(nums)     # Get an iterator from a list

print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
# print(next(it))   # Raises StopIteration

#Example of a generator:
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

#Generator Expression (like list comprehension):
gen = (x*x for x in range(3))
print(list(gen))  # [0, 1, 4]

#Example: Compare list vs generator
# List (eager - memory-heavy)
squares = [x*x for x in range(1000000)]  # Uses a lot of memory

# Generator (lazy)
squares_gen = (x*x for x in range(1000000))  # Uses very little memory

'''
What is an Iterator?
An iterator is any object in Python that implements:
__iter__()  → returns the iterator object itself  
__next__()  → returns the next item or raises StopIteration

Common iterators: list iterators, file objects, zip/map/filter, etc.

What is a Generator?
A generator is a simpler way to create iterators using yield instead of returning a full list.
It automatically implements __iter__() and __next__().

Use Cases:
Iterator	                           Generator
When using iter() manually	           When processing large/streamed data
Custom iteration logic	               Memory-efficient data pipelines
Reading files line-by-line	           Infinite sequences or lazy streams

Performance & Memory:
Feature	               Iterator	                       Generator
Memory	               Depends on data                 Extremely memory efficient (lazy eval)
Speed	               Slightly faster if in memory	   Faster for streamed or partial output
Complexity	           More boilerplate                Cleaner with yield

Best Practices:
Use generators when:
Processing large datasets
Working with I/O (e.g., reading files)
Infinite or long-running sequences

Use iterators when:
You need more control (e.g., manual __next__())
Building custom iterable objects


Key Differences
Feature	                Iterator	                            Generator
How it's created	    Class with __iter__() & __next__()	    Function using yield
Syntax	                Verbose	                                Short and readable
Memory Usage	        Manual	                                Automatically lazy & memory efficient
Use case	            Custom control	                        Best for streaming/large data
State management	    Handled manually	                    Handled by Python



yield pauses the function and returns control to the caller.
The function can resume from where it left off when next() is called again.
Generator functions using yield return a generator object, which is an iterator under the hood.

Feature	           return	                                yield
Purpose	           Ends a function and returns a value	    Pauses the function and yields a value
Execution	       Function exits completely	            Function suspends, resumes later
Return value       A value (any type)	                    A generator object (iterator)
Reusability	       Cannot resume execution	                Can resume from where it left off
Use case	       One-time value output	                Streaming or producing multiple values over time


'''