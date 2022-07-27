class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0  #keep track of zeroes
        j = 0  #keep track of elements in the list
        
        for j in range (len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
        