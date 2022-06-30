class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        print(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            return nums[2]
#         lts = []
#         for i in nums:
#             if i not in lts:
#                 lts.append(i)
        
#         lts.sort(reverse=True)
#         if len(lts) < 3:
#             return max(lts)
#         else:
#             return lts[2]