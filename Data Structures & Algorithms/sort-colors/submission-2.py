class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        """Sorting Approach"""
"""
        count0=0
        count1=0
        count2=0
        for num in nums:
            if num==0:
                count0+=1
            elif num==1:
                count1+=1
            else:
                count2+=1
        i=0
        for _ in range(count0):
            nums[i]=0
            i+=1
        for _ in range(count1):
            nums[i]=1
            i+=1

        for _ in range(count2):
            nums[i]=2
            i+=1
        """

        #Optimal Approach: Dutch National Flag
