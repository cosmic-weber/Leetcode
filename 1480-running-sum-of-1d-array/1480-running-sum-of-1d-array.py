class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        lst.append(nums[0])
        for i in range(1, len(nums)):
            lst.append(lst[i-1]+nums[i])
            
        return lst