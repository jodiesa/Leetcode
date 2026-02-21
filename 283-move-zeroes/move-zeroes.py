class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #my solution idea  for problem 283 
        #1. Create new array
        #2 intitlise left pointer "l" and right pointer "r"
        #3 for loop , while i is at the first index
        #4 while the "l" is more than 0 , increment movement of "l"
        #5 else, assign r to the "0" and move it to the back
        #continue until end of array
        #6 append all to new array

        #neetcode sol
        l = 0  #init l pointer
        for r in range(len(nums)):
            if nums[r] != 0: #For each non-zero element, copy it to nums[l] and increment l.
                 nums[l] = nums[r]
                 l += 1

        while l < len(nums): #Second pass: Fill positions from l to the end with 0.
            nums[l] = 0
            l += 1