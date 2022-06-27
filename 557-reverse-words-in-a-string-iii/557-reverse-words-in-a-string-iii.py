class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        for i in s.split():
            lst.append(i)
        s = ''
        for i in range(len(lst)):
            s += lst[i][::-1]
            if i == len(lst) - 1:
                break
            s += ' '
        
        return s