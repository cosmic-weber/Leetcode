class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstsearch(nums, target),self.lastsearch(nums, target)]
        
    def firstsearch(self, nums, target):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                i = mid
                r = mid - 1
                
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return i
        
    def lastsearch(self, nums, target):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                i = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return i
