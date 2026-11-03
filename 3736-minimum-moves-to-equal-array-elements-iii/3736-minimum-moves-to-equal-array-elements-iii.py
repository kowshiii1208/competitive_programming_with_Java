class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        res = 0
        for i in nums:
            if i<mx:
                res+=mx-i
        return res