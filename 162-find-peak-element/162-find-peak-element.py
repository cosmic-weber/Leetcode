class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return nums.index(max(nums))
        return self.binarySearch(0, len(nums)-1, nums)
        
    def binarySearch(self, l, r, nums):
        if l == r:
            return l
        mid  = l + (r - l) / 2
        mid  = int(mid)
        if nums[mid] > nums[mid + 1]:
            return self.binarySearch(l, mid, nums)
        return self.binarySearch(mid+1, r, nums)
        
        
        