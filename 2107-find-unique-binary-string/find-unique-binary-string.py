class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []

        # Using Cantor's Diagonlization
        for i in range(len(nums)):
            if (nums[i][i] == '0'):
                res.append('1')
            else:
                res.append('0')
        
        return ''.join(res)