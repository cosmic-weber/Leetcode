from collections import Counter
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        if not words or not s:
            return 0
        
        ans = len(words)
        for word in words:
            index = -1
            for c in word:
                index = s.find(c, index+1)
                if index == -1:
                    ans -= 1
                    break
        return ans