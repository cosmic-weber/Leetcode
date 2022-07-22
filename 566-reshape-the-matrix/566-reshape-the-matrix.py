class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c: 
            return mat
        
        new_mat, cur_row, count = [], [], 0 
        for row in mat:
            for el in row:
                count+=1
                if count < c:
                    cur_row.append(el)
                else:
                    cur_row.append(el)
                    new_mat.append(cur_row)
                    cur_row, count = [], 0
        return new_mat