class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        n = len(nums)
        l, r = 0, n-1
        
        i = 0
        while i <= r:
            if nums[i] == 0:
                self.swap(l, i, nums)
                l += 1
            elif nums[i] == 2:
                self.swap(r, i, nums)
                r -= 1
                i -= 1
            i += 1
        
    def swap(self, pointer, index, nums):
        temp = nums[index]
        nums[index] = nums[pointer]
        nums[pointer] = temp