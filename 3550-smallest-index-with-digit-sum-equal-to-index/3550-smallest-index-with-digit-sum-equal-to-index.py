class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(str(nums[i]))==1 and nums[i]==i:
                return i
                break
            s = sum(int(j) for j in str(nums[i]))
            if s==i:
                return i
        return -1