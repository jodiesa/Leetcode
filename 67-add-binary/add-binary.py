class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #thought process : 
        # if 1 + 1 = 2, the "carry" will be 1
        # value would be 2%2= 0, carry will be sum / 2 , e.g (2/2=1)
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1

            if j >= 0:
                carry += int(b[j])
                j -= 1

            s.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(s))