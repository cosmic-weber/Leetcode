import math
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        boxTypes.sort(key = lambda x: -x[1])
        Sum=0
        print(boxTypes)
        for i in boxTypes:
            truckSize -= i[0]
            if truckSize >= 0:
                Sum += i[0] * i[1]
            if truckSize < 0:
                Sum += (i[0]+truckSize) * i[1]
                break
           
            
        return Sum