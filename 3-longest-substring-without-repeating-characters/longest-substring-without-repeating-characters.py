class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set() #track duplicates
        l = 0
        longest = 0
        n = len(s) # ab c d e a =7
        for r in range(n):  #o(n) in range of a b c d e a
            while s[r] in charSet:  #duplicate found
                charSet.remove(s[l])
                l += 1   #move pointer l
            w = ( r - l) + 1 #length
            longest = max(longest,w)
            charSet.add(s[r])
        return longest