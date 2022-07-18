class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        m,n = len(word1), len(word2)
        for i in range(m):
            s+=word1[i]
            if i < n:
                s+=word2[i]
            if m < n and i == m - 1:
                s+=word2[i+1:]
                break
            if n < m and i == n - 1:
                s+=word1[i+1:]
                break
        return s