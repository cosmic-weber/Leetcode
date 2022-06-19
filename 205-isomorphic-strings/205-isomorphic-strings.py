from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = Counter(s), Counter(t)
        lst1, lst2 = [], []
        for i in d1.values():
            lst1.append(i)
        
        for j in d2.values():
            lst2.append(j)
            
        print(lst1, lst2)
        
        return [s.index(m) for m in s] == [t.index(n) for n in t] 
        
        
        
        