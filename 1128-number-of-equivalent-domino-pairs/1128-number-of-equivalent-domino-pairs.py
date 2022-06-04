from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        d = {}
        pairs = 0
        for i in dominoes:
            x, y = max(i), min(i)
            if (x, y) not in d:
                d[(x, y)] = 1
                # print(d)
            else:
                pairs += d[(x, y)]
                d[(x, y)] += 1
                
        return pairs