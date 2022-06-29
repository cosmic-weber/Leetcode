class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        lst = []
        for i in points:
            if i[0] == x or i[1] == y:
                lst.append((i,points.index(i)))
        if lst == []:
            return -1
        lst1 = []
        for i in lst:
            d = abs(x-i[0][0]) + abs(y-i[0][1])
            lst1.append((d,i[1]))
        lst1.sort()
        return lst1[0][1]