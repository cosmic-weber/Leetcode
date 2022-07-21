class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l,r = 0,1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l+=1
            r+=1
        return False
        # nums_dict = collections.Counter(nums)
        # for i in nums_dict.values():
        #     if i > 1:
        #         return True
        # return False