class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #negavtive number is false immdiately
        #number ending with 0 is false immdiately
        # exception is number 0 itself
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        half = 0 #reverse part of number
            #when x is greater than half
        while x > half:
            half = (half * 10) + (x % 10) #multiply half by 10 
            x = x // 10 #floor dviision 

        return x == half or x == half // 10 #half and x is same x ==half

        #reading backwards and forwards is same 
        #convert to string, then reverse string (But cannot)
        #just reverse half the number
