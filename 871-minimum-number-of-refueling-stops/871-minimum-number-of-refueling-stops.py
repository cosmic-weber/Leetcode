class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        arr = [startFuel] + [0] * len(stations)
        
        for i in range(len(stations)):
            for j in range(i, -1, -1):
                if arr[j] >= stations[i][0]:
                    arr[j+1] = max(arr[j+1], arr[j]+stations[i][1])
        
        for m, n in enumerate(arr):
            if n >= target:
                return m
            
        return -1