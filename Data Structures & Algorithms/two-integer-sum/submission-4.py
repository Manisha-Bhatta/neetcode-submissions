class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in mp:
                return [mp[sub],i]
            mp[nums[i]]=i
        return []