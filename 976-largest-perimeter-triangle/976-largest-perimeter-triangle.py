class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        area = 0
        nums.sort()
        print(nums)
        for i in range(len(nums)-3, -1, -1):
            if nums[i+1] + nums[i] > nums[i+2]:
                area = nums[i+2] + nums[i] + nums[i+1]
                return area
        return 0