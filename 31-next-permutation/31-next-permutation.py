class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)-2
        
        while m >= 0:
            if nums[m] < nums[m+1]:
                break
            
            m -= 1
        
        if m < 0:
            nums.sort()
            return
        
        for i in range(len(nums)-1,m,-1):
            if nums[i] > nums[m]:
                nums[i], nums[m] = nums[m], nums[i]
                break
                
        nums[m+1:] = nums[m+1:][::-1]
