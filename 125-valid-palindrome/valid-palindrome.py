class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #.isalnum() --> is this alphamumeric (a-z,A-Z,0-9) if yes --> true , if no --> false
        #.lower() --> convert to lowercase (A--> a) <lowercase string> 
        l = 0
        r= len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
            