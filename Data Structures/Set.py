# A set is an unordered collection with no duplicate elements
# Basic uses include membership testing and eliminating duplicate entriese 


def createSets1() -> set:
    aSet = set()

print(createSets1())

def createSets2() -> set:
    basket = {'apple', 'orange', 'pear', 'banana'}
    return basket
print(createSets2())

def inSet(item: str, aSet: set) -> bool:
    return item in aSet

print(inSet('apple', createSets2()))
print(inSet('watermelon', createSets2()))

def createSets3() -> set:
    return set('aacjsndlemjsx')

# it will eliminate the duplicates from the set 
print(createSets3())

# test set opetations 
a = set('abcdefg')
b = set('acefghijk')
# in a not in b
print(a - b)
# in a or in b
print(a | b)
# in a and in b
print(a & b)
# in a or b but not in both
print(a ^ b)

def set_comprehensions() -> set:
    return {x for x in 'abcdefg' if x not in 'abc'}

print(set_comprehensions())    
