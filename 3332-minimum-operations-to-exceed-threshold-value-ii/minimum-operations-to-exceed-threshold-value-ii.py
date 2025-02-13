class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = [num for num in nums if num < k]
        heapq.heapify(arr)

        op = 0
        while arr:
            x = heapq.heappop(arr)
            op += 1

            if not arr:
                break
            
            y = heapq.heappop(arr)
            key = x * 2 + y

            if key < k:
                heapq.heappush(arr, key)

        return op