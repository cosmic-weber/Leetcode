class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h1, w1 = max(horizontalCuts[0], h-horizontalCuts[-1]), max(verticalCuts[0], w-verticalCuts[-1])
        if len(horizontalCuts) > 1:
            for x in range(1, len(horizontalCuts)):
                h1 = max(h1, horizontalCuts[x]-horizontalCuts[x-1])
        
        if len(verticalCuts) > 1:
            for x in range(1, len(verticalCuts)):
                w1 = max(w1, verticalCuts[x]-verticalCuts[x-1])
                
        return h1 * w1 % (10**9+7)