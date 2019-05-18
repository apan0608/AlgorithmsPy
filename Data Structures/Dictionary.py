# can use tuple as a key is the tuple only stores mutable values 
# if stores a key that already in the usem the old value associated 
# with the key will be replaced 
# list(d) returns a list of all the keys used in the dictionary in insertion order 
# sorted(d) will return sorted
# use in keyword to check if a key is already in dictionary

def createDict_1() -> dict:
    return {'jack': 300, 'emma': 211, 'sape': 100}

print(createDict_1())

def delete_item(items: dict) -> dict:
    del items['emma']
    return items

print(delete_item(createDict_1()))

print(list(createDict_1()))
print(sorted(createDict_1()))

print('emma' in createDict_1())

print('emma' not in createDict_1())

# this one uses constructor 
def createDict_2() -> dict:
    return dict([(1, 'item 1'), (2, 'item 2'), (3, 'item 3')])

def comprehensions() -> dict:
    return {x: x ** 2 for x in (2, 4, 6)}

print(comprehensions())

def createDict_3() -> dict: 
    return dict(item1 = 1, itme2 = 2, item3 = 4)
print(createDict_3())