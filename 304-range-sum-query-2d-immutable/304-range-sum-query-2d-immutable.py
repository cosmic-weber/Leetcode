class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, col = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (col+1) for _ in range(rows)]
        
        for i in range(rows):
            for j in range(col):
                self.sum_matrix[i][j+1] = self.sum_matrix[i][j] + matrix[i][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        row = row1
        while row <= row2:
            sum_ += self.sum_matrix[row][col2+1] - self.sum_matrix[row][col1]
            row += 1
        return sum_


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)