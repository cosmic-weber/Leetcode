class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = sum(nums)
        

    def update(self, index: int, val: int) -> None:
        self.sum -= self.nums[index]
        self.nums[index] = val
        self.sum += val

    def sumRange(self, left: int, right: int) -> int:
        l = sum(self.nums[:left])
        r = sum(self.nums[right+1:])
        return self.sum - (l+r)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)