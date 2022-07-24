class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #dutch national flag approach
        
        i=0
        j=0
        pivot=1
        k=len(nums)-1
        
        while j <= k:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            elif nums[j] > pivot:
                nums[j], nums[k] = nums[k], nums[j]
                k-=1
            else:
                j+=1
            
            
        