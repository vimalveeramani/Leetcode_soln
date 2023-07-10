class Solution:
    def twoSum(Self,nums,target):
        ans=[]
        map={}
        for i in range (len(nums)):
            diff=target-nums[i]
            if diff not in map:
                map[nums[i]]=i
            else:
                ans.append(i)
                ans.append(map[diff])
        return ans
