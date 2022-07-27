class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0  #keep track of zeroes
        j = 0  #keep track of elements in the list
        if len(nums)>0:
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    j += 1

        return nums
        