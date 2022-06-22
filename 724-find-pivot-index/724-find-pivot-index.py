class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = -1
        left_sum, right_sum = 0, 0
        n = len(nums)
        
        for i in range(n):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return index
    