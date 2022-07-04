class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        lst = []
        for i in range(len(arr)+1):
            for j in range(i):
                lst.append(arr[j:i])
        sum_ = 0
        for x in lst:
            if len(x) % 2 == 0:
                lst.remove(x)

        for x in lst:
            sum_ += sum(x)
        return sum_