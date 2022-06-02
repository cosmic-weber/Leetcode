class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        lst, lst1 = [], []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                lst.append(matrix[j][i])
            lst1.append(lst)
            lst = []
        
        return lst1