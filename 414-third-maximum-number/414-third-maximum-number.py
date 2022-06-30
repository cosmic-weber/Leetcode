class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        lts = []
        for i in nums:
            if i not in lts:
                lts.append(i)
        
        lts.sort(reverse=True)
        if len(lts) < 3:
            return max(lts)
        else:
            return lts[2]