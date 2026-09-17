class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # mx = float('-inf')
        # mn = float('inf')
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         pro = nums[i]*nums[j]
        #         if pro>mx:
        #             mx = pro
        #         elif pro<mn:
        #             mn = pro
        # return mx-mn
        nums.sort()
        return (nums[-1]*nums[-2])-(nums[0]*nums[1])
                