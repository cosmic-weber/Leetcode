class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            n = (low + high) // 2
            if nums[n] == target:
                return n
            elif nums[n] > target:
                high = n - 1
            elif nums[n] < target:
                low = n + 1
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
