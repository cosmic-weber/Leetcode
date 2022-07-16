class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst, lst1 = [], []
        for num in nums1:
            i = nums2.index(num)
            if i == len(nums2)-1:
                lst.append(-1)
                continue
            lst1 = nums2[i+1:]
            for j in lst1:
                if j > nums2[i]:
                    lst.append(j)
                    break
            else:
                lst.append(-1)
            lst1 = []
            
        return lst