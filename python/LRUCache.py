from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.map=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self.map.keys():
            value=self.map[key]
            self.map.move_to_end(key)
            return value
        else:
            return  -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.map[key]=value
            self.map.move_to_end(key)
        else:
            if len(self.map)>=self.capacity:
                self.map.popitem(last=False)
            self.map[key]=value
            self.map.move_to_end(key)

lRUCache = LRUCache(2);
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))   # return 3
print(lRUCache.get(4))   # return 4