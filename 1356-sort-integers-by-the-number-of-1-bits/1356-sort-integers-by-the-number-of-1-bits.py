from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dct = defaultdict(list)
        count=0
        for i in arr:
            s = bin(i)[2:]
            dct[s.count('1')].append(i)
        lst=[]
        for j in sorted(dct.keys()):
            lst += sorted(dct[j])
        return lst