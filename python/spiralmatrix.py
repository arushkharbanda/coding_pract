from util import check
class Solution:
    def spiralOrder(self, matrix):
        result=[]
        m=len(matrix)
        if m>0:
            n=len(matrix[0])
        else:
            return []
        while len(result)<m*n:
            try:
                #top
                top=matrix[0]
                result.extend(top)
                del matrix[0]


                #right
                right=[]
                for row in matrix:
                    right.append(row[len(row)-1])
                    del row[len(row)-1]
                result.extend(right)

                #bottom:
                bottom=matrix[len(matrix)-1]
                bottom.reverse()
                result.extend(bottom)
                del matrix[len(matrix)-1]

                # left:
                left=[]
                for row in matrix:
                    left.append(row[0])
                    del row[0]
                left.reverse()
                result.extend(left)
            except:
                pass
        return result


sol=Solution()
check([[[ 1, 2, 3 ],[ 4, 5, 6 ], [ 7, 8, 9 ]]],[[1,2,3,6,9,8,7,4,5]], sol.spiralOrder)
check([[[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]],[[1,2,3,4,8,12,11,10,9,5,6,7]], sol.spiralOrder)
check([[[3],[2]]],[[3,2]], sol.spiralOrder)

