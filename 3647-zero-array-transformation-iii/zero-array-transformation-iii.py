class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        edges = defaultdict(list)

        for st, en in queries:
            edges[st].append(en)
        
        lines = [0] * (n + 1)

        heap = []
        curr = 0

        for idx, num in enumerate(nums):
            if idx in edges:
                for en in edges[idx]: 
                    heappush(heap, -en)
            
            curr += lines[idx]
            while curr < num:
                if not heap or -heap[0] < idx:
                    return -1
                
                en = -heappop(heap)
                curr += 1
                lines[en + 1] -= 1
        
        return len(heap)