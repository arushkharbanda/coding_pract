from util import check
class Solution:
    def findDuplicates(self, nums):
        if len(nums) == 0:
            return []
        emap = {}
        rmap = {}
        #tmap = {}
        for x in nums:
            if x not in emap:
                emap[x] = True
                continue
            if x in emap :#and x not in tmap:
                rmap[x] = True
                continue
            '''
            if x in rmap:
                rmap.pop(x)
                tmap[x] = True
                continue
            '''
        return list(rmap)
sol=Solution()
check([[]], [[]], sol.findDuplicates)
check([[4,3,2,7,8,2,3,1]], [[2,3],[3,2]], sol.findDuplicates)
check([[1,	2,	3,	4,	5,	6,	21,	22,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,]], [[21,22]], sol.findDuplicates)
