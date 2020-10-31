from util import check
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        for r in range(len(height)):
            if height[r] >= height[l] and r == l + 1:
                l = r
            elif height[r] >= height[l] and r != l:
                water += pool_calc(height, l, r)
                l = r

        height = height[::-1]
        r = l
        l = 0
        for r in range(len(height)-r):
            if height[r] >= height[l] and r == l + 1:
                l = r
            elif height[r] >= height[l] and r != l:
                water += pool_calc(height, l, r)
                l = r
        return water

def pool_calc(height, l, r):
    w_height = min(height[l], height[r])
    l += 1
    water = 0
    while l < r:
        water += w_height - height[l]
        l += 1

    return water
sol=Solution()
check([[4,2,0,3,2,5]],[9], sol.trap)
check([[0,1,0,2,1,0,1,3,2,1,2,1]],[6], sol.trap)
