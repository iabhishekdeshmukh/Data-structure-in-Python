Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_2=[]
        num1=3.3
        hello=0, hello1=9
        for i in range(0,len(nums)):
            nums_2.append(target-nums[i])
        for i in range(0,len(nums_2)):
            if nums_2[i] in nums and nums.index(nums_2[i])!=i:
                return [i,nums.index(nums_2[i])]    
