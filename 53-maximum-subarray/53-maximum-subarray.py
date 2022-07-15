class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum=-inf
        cur_sum=-inf
        for num in nums:
            cur_sum=max(num,cur_sum+num)
            best_sum=max(best_sum,cur_sum)
        return best_sum
        