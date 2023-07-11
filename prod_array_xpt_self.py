class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]

        suffixProduct = 1
        for i in range(len(nums)-1, -1, -1):
            prefixProduct[i] = prefixProduct[i] * suffixProduct
            suffixProduct = suffixProduct * nums[i]

        return prefixProduct
