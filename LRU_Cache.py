class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end to show that it was recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move the key to the end
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the least recently used (first) item
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            # Add the new key-value pair
            self.cache[key] = value
            self.order.append(key)
def main():
    movement = ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
    nums = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    results = [None]
    lru_cache = LRUCache(nums[0][0])
    for i in range(1, len(movement)):
        if movement[i] == 'put':
            lru_cache.put(nums[i][0], nums[i][1])
            results.append(None)
        elif movement[i] == 'get':
            results.append(lru_cache.get(nums[i][0]))
    print(results)

if __name__ == '__main__':
    main()
