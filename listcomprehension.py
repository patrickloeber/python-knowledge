# avoid for loops!
squares = []
for i in range(5):
    squares.append(i * i)
print(squares)

# better: use list comprehension
# new_list = [expression for member in iterable]
squares = [i * i for i in range(5)]
print(squares)

# iterable can be a list, set, sequence, generator, or any other iterable
# expression can be a function
def cube(i):
    return i*i*i

cubes = [cube(i) for i in range(5)]
print(cubes)

# filter
# new_list = [expression for member in iterable (if conditional)]
evens = [i for i in range(20) if i%2 == 0]
print(evens)

def is_even(i):
    return i%2 == 0

evens = [i for i in range(20) if is_even(i)] 
print(evens)   

# modify
# new_list = [expression (if else conditional) for member in iterable]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10 if i > 5 else 0 for i in a]
print(b)

# set comprehension
quote = "hello everybody"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

squares = {i: i * i for i in range(5)}
print(squares)

# nested list comprehension
# use sparely!
matrix2d = [[i*j for i in range(5)] for j in range(1,3)]
print(matrix2d)

# A list comprehension in Python works by loading the entire output list into memory
# use genereator for large data!
# generators can also be created with generator expressions: 
# new_generator = (expression for i in iterable)

s = sum([i * i for i in range(1000)])
print(s)

s = sum((i * i for i in range(1000)))
print(s)

import sys
l = [i * i for i in range(1000)]
print(sys.getsizeof(l), "bytes")
g = (i * i for i in range(1000))
print(sys.getsizeof(g), "bytes")

# a word about speed:
# somtetimes it can be faster, but this may not always be the case!
from timeit import default_timer as timer
start = timer()
a = [i*i for i in range(1_000_000)]
stop = timer()
print(f'{stop-start:.4f} seconds')

start = timer()
a = []
for i in range(1_000_000):
    a.append(i*i)
stop = timer()
print(f'{stop-start:.4f} seconds')
