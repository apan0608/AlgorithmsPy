class Iterator:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.index = -1

    @staticmethod
    def loopUsingIterator():
        numbers = [1, 2, 3, 4, 6, 5, 8, 9]
        iter1 = numbers.__iter__() # or use iter(numbers)
        keepGoing = True
        while keepGoing:
            try: 
                print(iter1.__next__()) # or use next(numbers)
            except StopIteration:
                keepGoing = False

    def next(self) -> int:
        if self.index + 1 < len(self.numbers):
            self.index += 1
        else: 
            self.index = 0
        return self.numbers[self.index]

            # raise StopIteration("No items anymore")

       

# iter = Iterator([1, 6, 7, 3])
# print(iter.next())

Iterator.loopUsingIterator()

