class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l =0
        r= len(nums)-1
        while l< r:
            total= nums[l]+nums[r]
            if total==target:
                return [l+1,r+1]
            if total<target:
                l+=1
            else:
                r-=1
        return [-1,-1]