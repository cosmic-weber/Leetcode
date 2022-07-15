class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        r = len(grid)
        c = len(grid[0])
        
        def calculate_area(grid, h, v):
            if (h >= 0 and h < r) and (v >= 0 and v < c) and grid[h][v] == 1:
                grid[h][v] = 0
                c_area = 1 + calculate_area(grid,h+1,v)+calculate_area(grid,h-1,v)+calculate_area(grid,h,v-1)+calculate_area(grid,h,v+1)
                return c_area
            return 0
        
        for i in range(r):
            for j in range(c):
                area = max(area, calculate_area(grid, i, j))
        return area
                