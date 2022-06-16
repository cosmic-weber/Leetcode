class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        lst = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                lst.add(nums1[i]) 
                
        lst = list(lst)
        return lst