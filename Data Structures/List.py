# List can be used as queue or stack
# to gain good performance, use from collection import deque 

from collections import deque
def useQueue():
    queue = deque(['Eric', 'John', 'Michael'])
    queue.append('Terry')
    queue.append('Graham')
    queue.popleft()
    queue.pop()

# calculate square
squares = [x**2 for x in range(10) if x > 1]
print(squares)

# remove space
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
fruits = [weapon.strip() for weapon in freshfruit] 
print(fruits)

# get tuples
tuples = [(x, x**2) for x in range(6)]
print(tuples)

# nested lists
nested = [[1,2,3], [2,3,4], [3,4,5]]
breakIt = [item for sublist in nested for item in sublist]
# breakIt = [item for item in sublist for sublist in  nested ] # name sublist is not defined
print(breakIt)

# pi
from math import pi
pis = [str(round(pi, i)) for i in range(1, 6)]
print(pis)

# divide the matrix by index 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

divided = [[row[i] for row in matrix] for i in range(4) ]
print(divided)

# the above can be written this way
for i in range(4):
    transported = [[row[i] for row in matrix]]
print(transported)

# or using the built-in functions
built_in = list(zip(*matrix))
print(built_in)

# del
# del a[2:3]
# del a[:] # delete all 

