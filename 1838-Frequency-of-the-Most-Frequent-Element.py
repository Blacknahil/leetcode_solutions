class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        left=0
        n=len(nums)
        prefix=0
        _max=0
        for right in range(n):
            prefix+=nums[right]
            while nums[left]*(right-left+1)>prefix+k:
                prefix-=nums[left]
                left+=1
            _max=max(_max,right-left+1)
        
        return _max
        