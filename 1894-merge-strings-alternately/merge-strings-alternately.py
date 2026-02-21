class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        w1 = len(word1) #calculate the length of word1
        w2 = len(word2)
        l=min(w1,w2) #calculate min length of variable 1
        for i in range(l): #This loop will merge characters from both words alternately.
            merged += word1[i] + word2[i] #Inside the loop, concatenate the i-th character of word1 with the i-th character of word2 and add the result to the merged string.
        if w1 == w2:
            return merged
        elif w1 > w2:
            return merged + word1[l:] #If word1 is longer, append the remaining characters of word1 (starting from index l onward) to the merged string.
        elif w1 < w2:
            return merged + word2[l:] #If word2 is longer, append the remaining characters of word2 (starting from index l onward) to the merged string.