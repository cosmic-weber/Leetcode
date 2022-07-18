import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        l = collections.Counter(s)
        t = collections.Counter(t)
        
        for i in t:
            if t[i] != l[i]:
                return i

          