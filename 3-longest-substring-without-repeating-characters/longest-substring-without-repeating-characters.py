class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set() #keeps track of characters currently inside the window.
        l = 0  # l is the left pointer of the sliding window.It marks where the current substring starts.
        longest = 0 #Stores the maximum length of a valid substring found so far.
        n = len(s) # example : ab c d e a =7
        for r in range(n):  #o(n) r is the right pointer of the sliding window. It expands the window one character at a time
            while s[r] in charSet:  #char r in window, have duplicate
                charSet.remove(s[l]) #remove char at current l position, move l to the right as until no dup
                l += 1   #move pointer l
            w = ( r - l) + 1 #length , + 1 cause need to account that the ends are inclusive
            longest = max(longest,w)  #compare window length with previous, keep bigger one
            charSet.add(s[r]) #Add the current character to the set. now the window is valid again (no duplicates).
        return longest