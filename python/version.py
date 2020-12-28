from util import check

class Solution:
    def compareVersion(self, version1: str, version2: str):
        # Split by .
        v1=version1.split('.')
        v2=version2.split('.')

        # Go through array if exception return 0
        for i in range(len(v1)):
            try:
                v1_i_int=int(v1[i])
                v2_i_int=int(v2[i])
                if v1_i_int<v2_i_int:
                    return -1
                elif v1_i_int>v2_i_int:
                    return 1
            except:
                return 0
        return 0


sol=Solution()
#check(["1.01",  "1.001"],[0],sol.compareVersion)
#check(["1.0", "1.0.0"], [0],sol.compareVersion)
#check(["0.1",  "1.1"], [-1],sol.compareVersion)
check(["1.0.1", "1"], [1],sol.compareVersion)
#check(["7.5.2.4", "7.5.3"], [-1],sol.compareVersion)
#check(["", "7.5.3"], [0],sol.compareVersion)
#check(["7.5.2.4", ""], [0],sol.compareVersion)
