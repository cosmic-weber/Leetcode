class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, sum_ = len(mat), 0
        if n % 2 == 0:
            i = 0
            while i < n:
                sum_ += mat[i][i]
                i+=1
            i -= 1
            j = 0
            while j < n and i >= 0:
                sum_ += mat[i][j]
                j += 1
                i -= 1
            return sum_
        else:
            i = 0
            while i < n:
                sum_ += mat[i][i]
                i += 1
            i -= 1
            j = 0
            while j < n and i >= 0:
                if i == j:
                    j += 1
                    i -= 1
                    continue
                sum_ += mat[i][j]
                j += 1
                i -= 1
            return sum_