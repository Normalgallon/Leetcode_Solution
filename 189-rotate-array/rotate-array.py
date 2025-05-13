class Solution:
    def rotate(self, nums, k):
        nums.reverse()
        n=len(nums)
        k=k%n
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        
        return nums