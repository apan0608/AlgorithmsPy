class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        # the __update is replaced with _mapping__update and _mappingsubclass__update
        self.__update(iterable) # the update method in base class can override it 

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

# without using Miggling 
map = MappingSubclass([1,2,3,4,5])
for item in map.items_list:
    print(item)
