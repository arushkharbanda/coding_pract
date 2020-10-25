from util import check

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        # for all levels()
        for i in range(0,n//2):
            k = n - i - 1
            for r in range(i, n - i - 1):  # offset in layer
                j = n - r - 1
                matrix[r][i], matrix[k][r] = matrix[k][r], matrix[r][i]
                matrix[k][r], matrix[j][k] = matrix[j][k], matrix[k][r]
                matrix[j][k], matrix[i][j] = matrix[i][j], matrix[j][k]

sol=Solution()
m1=[[1,2,3],[4,5,6],[7,8,9]]
expected=[[7,4,1],[8,5,2],[9,6,3]]
m1_i=m1.copy()
sol.rotate(m1)
print("pass {} input {} output {} expected {}".format(m1==expected, m1_i, m1,expected))


m2=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
expected2=[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
m2_i=m2.copy()
sol.rotate(m2)
print("pass {} input {} output {} expected {}".format(m2==expected2, m2_i, m2,expected2))