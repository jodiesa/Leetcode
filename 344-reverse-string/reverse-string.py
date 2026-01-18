class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #easirst 2 pointer p[roblem]
        #cannot s[::-1]
       # [h,e,l,l,o]
       #0   1 2 3 4
       # s[L]         s[R]
       #1, swap 0 with 4
       #[o,e,l,l,h]
       #2 , swap 1 with 3, o,l,l,e,h

        n = len(s)
        l= 0
        r =n-1

        while l < r:
           s[l],s[r] = s[r], s[l] 
           l += 1 
           r -=1
        #time : 0(n)
        #space : o(1)