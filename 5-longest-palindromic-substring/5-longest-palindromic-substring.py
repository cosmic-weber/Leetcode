class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(string, left, right):
            nonlocal srt, max_
            while (left >= 0 and right < len(s)) and s[left] == s[right]:
                if right - left + 1 > max_:
                    max_ = (right - left + 1)
                    srt = s[left:right+1]
                left -= 1
                right += 1
        srt, max_ = "", 0 
        for i in range(len(s)):
            palindrome(s, i, i), palindrome(s, i, i+1)
        return srt
        
        
        # if len(s) == 1:
        #     return s
        # lst = []
        # dct = {}
        # for i in range(len(s)+1):
        #     for j in range(i):
        #         lst.append(s[j:i])
        # for m in lst:
        #     if m == m[::-1]:
        #         dct[m] = len(m)
        # max_, srt = 0, ""
        # for k in dct:
        #     if dct[k] > max_:
        #         max_ = dct[k]
        #         srt = k
        # return srt