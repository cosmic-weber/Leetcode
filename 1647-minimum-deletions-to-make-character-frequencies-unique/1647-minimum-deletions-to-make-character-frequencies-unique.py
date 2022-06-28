from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        lst = []
        # print(c)
        for d in c.values():
            lst.append(d)
        lst.sort(reverse=True)
        s = []
        for i in lst:
            if i not in s:
                s.append(i)
            else:
                i -= 1
                while i in s:
                    i -= 1
                if i == 0:
                    break
                s.append(i)
        # print(s)
        m = sum(s)
        n = sum(lst)
        # print(lst)
        return n - m