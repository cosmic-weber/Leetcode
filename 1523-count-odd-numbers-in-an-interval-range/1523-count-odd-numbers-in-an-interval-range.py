class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = (high - low) // 2
        if high % 2 != 0 or low % 2 != 0:
            n += 1
            return n
        return n
        