class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        suM, count = 0, 0
        
        l, r = 0, 0
        while r < len(nums):
            if nums[r] not in s:
                
                s.add(nums[r])
                count += nums[r]
                r+=1
                suM = max(suM, count)
            else:
                count -= nums[l]
                s.remove(nums[l])
                l+=1
        return suM
                
            
            