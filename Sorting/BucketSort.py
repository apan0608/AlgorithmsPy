class BucketSort():
    radix = 10

    def sort(self, items: list) -> list:
        buckets = [[] for i in range(self.getBucketSize(items))]
        for item in items:
            index = self.getIndex(item)
            subIndex = self.getInsertionOrder(buckets[index], item)
            buckets[index].insert(subIndex, item)
        merged = []
        for bucket in buckets:
            if len(bucket) > 0:
                merged.extend(bucket)
        print(merged)
        # for bucket in buckets:
            # print(bucket)
        # evenrually need to merge all the buckets into one 

  
    def getBucketSize(self, items: list) -> int:
        max = self.getMaximum(items)
        return int(max * self.radix)

    def getMaximum(self, items: list) -> int:
        return max(item for item in items)
    
    def getIndex(self, item: float) -> int:
        return int(item * self.radix) - 1

    def getInsertionOrder(self, items: list, item: float):
        length = len(items)
        if length == 0:
            return 0
        index = next((i for i in range(length) if items[i] > item), length)
        return index
            
sort = BucketSort()
items = [0.5, 0.2, 0.3, 1.7, 0.33, 0.56, 0.39, 0.4, 2.5]
sort.sort(items)

# buckets = [[] for i in range(20)]
# print(buckets[2])