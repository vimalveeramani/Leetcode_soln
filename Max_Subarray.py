class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        mx = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + curr)
            mx = max(mx, curr)
        return mx
