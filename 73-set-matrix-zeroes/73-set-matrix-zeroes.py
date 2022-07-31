class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lst, lst1= [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    lst.append(i)
                    lst1.append(j)
        print(lst)
        print(lst1)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in lst or j in lst1:
                    matrix[i][j] = 0
                    
        