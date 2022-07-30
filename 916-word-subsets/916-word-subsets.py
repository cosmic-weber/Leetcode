class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        c1 = Counter()
        for c in words2:
            c2 = Counter(c)
            for i in c2:
                c1[i] = max(c1[i], c2[i])
        # print(c1)
        lst = []
        for word in words1:
            m = Counter(word)
            count = 0
            for i in c1:
                if c1[i] > m[i]:
                    count = 1
                    break
            if count == 0:
                lst.append(word)
        return lst