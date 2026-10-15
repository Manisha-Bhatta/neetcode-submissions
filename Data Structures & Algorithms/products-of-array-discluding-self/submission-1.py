class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftProduct=[1]*n
        rightProduct=[1]*n
        result=[0]*n

        #Calculate product of all elements to the left
        for i in range(1,n):
            leftProduct[i]=leftProduct[i-1]*nums[i-1]
        
        #Calculate product of all elements to the right
        for i in range(n-2,-1,-1):
            rightProduct[i]=rightProduct[i+1]*nums[i+1]

        #Multiply right and left product
        for i in range(n):
            result[i]=leftProduct[i]*rightProduct[i]
        
        return result