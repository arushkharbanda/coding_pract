from util import check
class Solution:
    def hasOverlap(self,range, ranges):
        for i,r in enumerate(ranges):
            if (range[0]>r[0] and range[0]<r[1]) or (range[1]>r[0] and range[1]<r[1]):
                return i
        return -1

    def extendRange(self, initial, to_add):
        left=min(to_add[0], initial[0])
        right=max(to_add[1], initial[1])
        return (left, right)


    def partitionLabels(self, S):
        # 1. create dict
        # a-0,2,6,8.....
        # 2. Ranges=[]
        d={}
        for i,c in enumerate(S):
            if c in d:
                d[c].append(i)
            else:
                d[c]=[i]
        # all ranges are non overlapping
        ranges=[]
        for c in d.keys():
            l=d[c]
            overlap=self.hasOverlap((l[0],l[-1]),ranges)
            if overlap==-1:
                ranges.append((l[0],l[-1]))
            else:
                ranges[overlap]=self.extendRange(ranges[overlap],(l[0],l[-1]))
        return [(r[1]-r[0]+1) for r in ranges]

sol=Solution()
check(["ababcbacadefegdehijhklij"],[[9,7,8]], sol.partitionLabels)