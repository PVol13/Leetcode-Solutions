class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0,len(nums)):
            if nums[i]==target:
                found=1
                return i
                break
        j=0
        for j in range(0,len(nums)):
            if target<nums[0]:
                return 0
                break
            elif target>nums[len(nums)-1]:
                return len(nums)
                break
            elif nums[j]<target<nums[j+1]:
                return j+1
                break