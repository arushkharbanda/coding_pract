
def twoSum( nums, target: int):
    # Assuming that nums is not empty
    i=0
    j=len(nums)-1
    nums2=nums.copy()
    nums.sort()
    while(i<j):
        sum=nums[i]+nums[j]
        if sum==target:
            a=nums[i]
            b=nums[j]
            break
        elif sum>target:
            j=j-1
        elif sum<target:
            i=i+1
    ioa=nums2.index(a)
    iob=[i for i,x in enumerate(nums2) if x==b and i!=ioa ][0]
    return [ioa,iob]







print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))

#assert(twoSum([2,7,11,15],9)==[0,1])
#assert(twoSum([3,2,4],6)==[1,2])
#assert(twoSum([3,3],6)==[0,1])
