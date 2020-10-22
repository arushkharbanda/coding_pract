from util import check

class Solution:
    def findLength(self, A, B) -> int:
        arr_sub=[0 for i in range(len(A)+1)]
        arr=[arr_sub.copy() for j in range(len(B)+1)]
        max=0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1]:
                    arr[i][j]=arr[i-1][j-1]+1
                    if arr[i][j]>max:
                        max=arr[i][j]
        return max


sol=Solution()
check([[1,2,3,2,1],[3,2,1,4,7] ],[3], sol.findLength)
