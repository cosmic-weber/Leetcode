class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m =  len(nums)
        # for i in range(k):
        #     n = nums[-1]
        #     for j in range(m-1, 0, -1):
        #         nums[j] = nums[j-1]
        #     nums[0] = n
                
        if k > m:
            k = k % m
        nums[:] = nums[m-k:] + nums[0:m-k]