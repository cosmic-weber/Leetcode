class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = 0
        for i in d.values():
            res += i // 2 * 2
            if i % 2 == 1 and res % 2 == 0:
                res += 1
        return res