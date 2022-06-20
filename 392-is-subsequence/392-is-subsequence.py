class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
#         i, j, m, n = 0, 0, len(s), len(t)
        
#         while i < m and j < n:
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
        
#         return i == m
        m, n = len(s), len(t)
        if m == 0 and n == 0:
            return True
        if n == 0:
            return False
        if m == 0 and n != 0:
            return True
        if m > n:
            for i in range(n):
                if t[i] not in s:
                    return False
                j = s.index(t[i])
                s = s[j+1:]
        else:
            for i in range(m):
                if s[i] not in t:
                    return False
                j = t.index(s[i])
                t = t[j+1:]
        return True