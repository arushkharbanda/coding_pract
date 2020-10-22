from util import check
from math import floor

class Solution:
    def canPartition(self, nums) -> bool:
        # find half of total
        total=0
        for i in nums:
            total+=i
        if total%2==0:
            required_sum=floor(total/2)
        else:
            return False

        # create an array
        arr_sums=[None for x in range(required_sum+1)]
        arr=[arr_sums.copy() for x in range(len(nums))]

        # fill the matrix
        for i,element in enumerate(nums):
            for sum in range(required_sum+1):
                # can we make sum with or without element
                # based on can we make sum-element

                if sum-element>0 and i-1>0:
                    make_with=arr[i-1][sum-element]
                else:
                    make_with=(sum==element)

                if i-1>0:
                    make_wo=arr[i-1][sum]
                else:
                    make_wo=(sum==0)

                arr[i][sum]= make_wo or make_with
            if arr[i][required_sum]:
                return True
        return False


sol=Solution()
check([[1,5,11,5]], [True], sol.canPartition)
check([[1,2,3,5]],[False], sol.canPartition)
check([[1,2,5]],[False], sol.canPartition)
check([[2,2,3,5]],[False], sol.canPartition)


