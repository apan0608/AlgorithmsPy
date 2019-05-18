# TUole consistes of a number of values separated by commas
# Usually contain a heterogeneous elements 
# Accessed by index or unpacking or by attribute

from collections import namedtuple

def initialize_1() -> tuple:
    return 1233, 234, 555, 'hello'


def initialize_2() -> tuple:
    return ('new', 234, 555, 'hello')

def initialize_nested() -> tuple:
    return 'I am nested', ("in the nest", 1, 2,3), 3,4

def initialize_mutable() -> tuple:
    return 'I am nested', ["in the nest", 1, 2,3], 3,4   


def initialize_empty() -> tuple:
    return ()

def initialize_named_tuples() -> namedtuple:
    Car = namedtuple('Car', ('Colour', 'Rego'))    
    myCar = Car('Yellow', '1235')
    return myCar

def initialize_with_one() -> tuple:
    return (1)

def sequence_unpacking() -> tuple:
    t = 1, 2, 3, 4, 5,  # this is initialize with 5 items not 6
    x, y, z, a,b = t
    return x, y, z, a, b

t = initialize_1()
print(t[0])

t = initialize_2()
print(t[0])

nested = initialize_nested()
print(nested[0])
print(nested[1][0])

# message: tuple object does not support item assignment 
# t[0] = 'assign new' 

# but tuple can contain mutable objects 
t = initialize_mutable()
t[1][0] = 'assigning new value'
print(t[1][0])

#empty tuple 
empty = initialize_empty()
print(empty)

# named
named = initialize_named_tuples()
print(named)

# one item tuple
one_item = initialize_with_one()
print(one_item)

# tuple packing and sequence unpacking 
unpakcing = sequence_unpacking()
print(unpakcing)

print((1, '2') == (1, '2'))