class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lst = nums.count(0)
        for i in range(lst):
            nums.remove(0)
            nums.append(0)
        
        # l, r = 0, 0
        # while r < len(nums):
        #     if nums[l] == 0:
        #         nums.append(nums.pop(l))
        #     else:   l+= 1
        #     r += 1
                
        
# Additional Space approach
#         lst = []
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 lst.append(nums[i])
        
#         nums = [0] * len(nums)
        
#         for i in range(len(lst)):
#             nums[i] = lst[i]
#         print(nums)
        
        
# works on maximum testcase but not on all of them
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 nums.insert(-1, nums.pop(i))
#                 print('holo')
        
#         print(nums)
#         if 0 in nums and nums[-1] != 0:
#             for i in range(len(nums)):
#                 if nums[i] == 0:
#                     count  = i 
#                     break
#             nums.insert(count, nums.pop())