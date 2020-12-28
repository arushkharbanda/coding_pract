from util import check

class Solution:

    def rob_old(self, nums) -> int:
        total=sum(nums)
        arr_sub=[False for x in range(total+1)]
        arr=[arr_sub.copy() for x in range(len(nums))]
        max_int=0
        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)
        for i in range(len(nums)):
            arr[i][0]=True
            arr[i][nums[i]]=True
            if nums[i]>max_int:
                max_int=nums[i]

        for sums in range(total+1):
            for i,ele in enumerate(nums):
                if sums>nums[i] and i>1:
                    r=False
                    for p in range(0,i-1):
                        r=arr[p][sums-nums[i]] or r
                    arr[i][sums]=r or arr[i-2][sums]
                    if sums>max_int and arr[i][sums]:
                        max_int=sums
        return max_int

    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        f = [0] * len(nums)
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])
        return f[-1]



sol=Solution()
check([[1,2,3,1]],[4],sol.rob)
check([[2,7,9,3,1]],[12],sol.rob)
check([[]],[0],sol.rob)
check([[0]],[0],sol.rob)
check([[0,0]],[0],sol.rob)
check([[1]],[1],sol.rob)
check([[1,1]],[1],sol.rob)
check([[4,1,1,4]],[8],sol.rob)
check([[1,3,1]],[3],sol.rob)
check([[121,48,151,122,147,24,30,61,41,200,244,194,201,147,195,170,80,41,229,46,69,231,40,74,241,151,224,96,132,108,41,244,224,44,14,147,32,5,27,231,77,60,233,31,169,17,169,28,129,157,3,73,139,3,132,133,34,154,101,84,13,134,124,172,239,202,147,8,213,178,193,70,14,212,0,203,237,202,80,140,250,150,144,224]],[6233],sol.rob)
