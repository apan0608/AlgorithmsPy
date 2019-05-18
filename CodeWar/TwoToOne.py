def longest(s1, s2) -> list:
    aux =  initialize()
    for item in s1 + s2:
        markItem(item, aux)
    return getOrdered(aux)


def markItem(item: str, aux: list):
    index = getIndex(item)
    aux[index] = 1

def getIndex(letter: str)-> int: 
    digit = ord(letter)
    return digit - 97 # a is 97, a is 0

def initialize() -> list:
    # initial = [i for i in range(0, 26)] is faster than while or for 
    # arr = [[0 for i in range(no_of_cols)] for j in range(no_of_rows)]
    return [0] * 26 # fastest way to initialize lists, but not good for 2 dimentional 

def getOrdered(aux: list) -> str:
    result = ''
    for i in range(26):
        if aux[i] == 1:
            result += getLetter(i) 
    return result

def getLetter(index: int) -> str:
    return str(chr(index + 97))

def test1():
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    actual = longest(a, b)
    expected = "abcdefklmopqwxy"
    print(actual == expected)
    print('Actual is {} and expected is {}'.format(actual, expected))

def test2():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "xxxxyyyyabklmopq"
    actual = longest(a, b)
    expected = "abcdefghijklmnopqrstuvwxyz"
    print(actual == expected)
    print('Actual is {} and expected is {}'.format(actual, expected))

# print([0] * 26)

test2()