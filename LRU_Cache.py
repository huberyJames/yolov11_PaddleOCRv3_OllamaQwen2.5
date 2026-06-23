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