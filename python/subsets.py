from util import check
'''
class Solution:
    def subsets(self, nums):
        stack=[]
        result=[]
        stack.append([])
        while len(stack)>0:
            item=stack.pop()
            #if item not in result:
            result.append(item)
            not_present=[x for x in nums if x not in item]
            for element in not_present:
                new_list=list(item.copy())
                new_list.append(element)
                new_list.sort()
                new_list=frozenset(new_list)
                stack.append(new_list)
        return result
'''

class Solution:
    def subsets(self, nums):
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]

        return output

sol=Solution()
#check([[1,2,3]],[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]], sol.subsets)
#check([[]],[[]], sol.subsets)
check([[1,2,3,4,5,6,7,8,10,0]],[[]], sol.subsets)
