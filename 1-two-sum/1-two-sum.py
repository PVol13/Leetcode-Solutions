class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         
        for i in range(0, len(nums)):
            hashmap = nums[:i] + nums[i+1 :]
            if (target - nums[i]) in hashmap:
                j = hashmap.index((target - nums[i]))
                break
        if j < i:
            return [i,j]
        else:
            return [i,j+1]
    
                    
        