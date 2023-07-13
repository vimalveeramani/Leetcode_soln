class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mn = 1
        mx = 1
        for i in range(len(nums)):
            if nums[i]==0:
                mn = 1
                mx = 1
                ans = max(ans,nums[i])
                continue

            tmp=mn
            mn = min(nums[i], min(nums[i] * mn, nums[i] * mx))
            mx = max(nums[i], max(nums[i] * tmp, nums[i] * mx))
            ans = max(ans, mx)

        return ans
