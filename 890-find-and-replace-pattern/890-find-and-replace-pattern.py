class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def count(s):
            c = Counter(s)
            d = []
            l = 0
            for i in s:
                c[i] = [c[i],l]
                l += 1
            lst = []
            for i in range(len(s)):
                lst.append(c[s[i]])
            return lst
        ans = []
        m = count(pattern)
        print(m)
        for word in words:
            print(count(word))
            if m == count(word):
                ans.append(word)
        return ans
        