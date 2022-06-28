class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m,o = 1,0
        while n != 0:
            m *= n%10
            o += n%10
            n = n // 10
        return m - o
        