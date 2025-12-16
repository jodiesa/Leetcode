class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #for  list [int] > 0 <5

#x[1]+x[2]+x[3]+x[4]/4 =y
#y ...
        #contiguous = all elements must be together, cannot shift them around
             #    i                   5
        # nums = [1 ,12, -5, -6, 50, 3]

        curr_sum = sum(nums[:k]) #sum of nums up until index k 
        max_sum = curr_sum #max sum = curr sum
        for i in range(len(nums)-k):  #for i within the index stated in k
            curr_sum += nums[i + k] - nums[i] #i + k = 1 + all  number until index 5 which is until '3', then minus 1 as it is out of the sliding window
            max_sum = max(max_sum,curr_sum) #?
        return max_sum / float(k)