class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cur_max=cur_min=1
        for i in nums:
            temp=cur_max*i
            cur_max=max(temp,cur_min*i, i)
            cur_min=min(temp, cur_min*i,i)
            res=max(res, cur_max)
        return res